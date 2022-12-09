import aiohttp
import asyncio
import click


async def fetch_url(url, session):
    async with session.get(url) as resp:
        # time.sleep(1)
        data = await resp.read()

        if 'python' in data.decode().lower():
            return f'"Python" exists on the page {url}'
        else:
            return f'"Python" does not exists on the page {url}'


async def worker(queue, session):
    while True:
        url = await queue.get()
        try:
            res = await fetch_url(url, session)
            print(res)
        finally:
            queue.task_done()


async def fetch_batch_urls(queue, workers):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(worker(queue, session))
            for _ in range(workers)
        ]
        await queue.join()

        for task in tasks:
            task.cancel()


async def readline(urls_queue, input_filename):
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            await urls_queue.put(line)


async def process_urls(n_workers, urls_file):
    urls_queue = asyncio.Queue(maxsize=n_workers)
    gather = asyncio.gather(readline(urls_queue, urls_file),
                            fetch_batch_urls(urls_queue, n_workers)
                            )
    await gather


@click.command(name="main")
@click.argument('n_workers')
@click.argument('urls_file')
def main(n_workers, urls_file):
    asyncio.run(process_urls(int(n_workers), urls_file))


if __name__ == '__main__':
    main()
