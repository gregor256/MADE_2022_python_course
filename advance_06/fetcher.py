# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import asyncio
import aiohttp
import click

OUTPUT_Q_SIZE = 10


async def fetch_url(url, session):
    async with session.get(url) as resp:
        data = await resp.read()

        if 'python' in data.decode().lower():
            return f'"python" exists on the page {url}'
        return f'"python" does not exist on the page {url}'


async def dump_worker(_result_queue, filename):
    while True:
        processing_result = await _result_queue.get()
        try:
            with open(filename, 'a', encoding='utf-8') as output:
                print(processing_result, file=output)
        finally:
            _result_queue.task_done()


async def processing_worker(_urls_queue, _result_queue, session):
    while True:
        url = await _urls_queue.get()
        try:
            result = await fetch_url(url, session)
            await _result_queue.put(result)
        finally:
            _urls_queue.task_done()


async def fetch_batch_urls(_urls_queue, _result_queue, workers):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(processing_worker(_urls_queue, _result_queue, session))
            for _ in range(workers)
        ]
        await _urls_queue.join()

        for task in tasks:
            task.cancel()


async def write_processed_data(_result_queue, filename):
    task = asyncio.create_task(dump_worker(_result_queue, filename))
    if _result_queue.qsize() > 0:
        await _result_queue.join()
        task.cancel()


async def readline(urls_queue, input_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            await urls_queue.put(line)


async def process_urls(n_workers, urls_file, output_file):
    urls_queue = asyncio.Queue(maxsize=n_workers)
    result_queue = asyncio.Queue(maxsize=OUTPUT_Q_SIZE)
    gather = asyncio.gather(readline(urls_queue, urls_file),
                            fetch_batch_urls(urls_queue, result_queue, n_workers),
                            write_processed_data(result_queue, output_file)
                            )
    await gather


@click.command(name="main")
@click.argument('n_workers')
@click.argument('urls_file')
def main_url_processing(n_workers, urls_file, output_file='output.txt'):
    with open('output.txt', 'w', encoding='utf-8') as output:
        output.truncate()
    asyncio.run(process_urls(int(n_workers), urls_file, output_file))


if __name__ == '__main__':
    main_url_processing()  # pylint: disable=no-value-for-parameter
