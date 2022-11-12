"""Client"""
import socket
import time
import threading
import queue
import click

HOST = "127.0.0.1"
PORT = 5000


def send_url_to_server(current_queue):
    """send_url_to_server"""
    while True:
        try:
            url = current_queue.get()
        except queue.Empty:
            continue

        if url == 'death_pill_url':
            current_queue.put('death_pill_url')
            break

        with socket.socket() as current_socket:
            current_socket.connect((HOST, PORT))
            current_socket.sendall(url.encode())
            data = current_socket.recv(1024)
            print(data.decode())


@click.command(name="get_threads")
@click.argument('n_threads')
@click.argument('urls_file')
def multithreading_client(n_threads, urls_file):
    """multithreading_client"""
    active_queue = queue.Queue()
    client_threads = [
        threading.Thread(
            target=send_url_to_server,
            args=(active_queue,)
        )
        for _ in range(int(n_threads))
    ]
    start_time = time.time()
    for thread in client_threads:
        thread.start()

    with open(urls_file, 'r', encoding='utf-8') as url_file:
        for line in url_file:
            active_queue.put(line.strip())

    active_queue.put('death_pill_url')

    for thread in client_threads:
        thread.join()
    print(f'\nTotal time: {round(time.time() - start_time, 3)} sec.')


if __name__ == '__main__':
    multithreading_client()  # pylint: disable=no-value-for-parameter
