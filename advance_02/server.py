"""Server"""
import socket
from collections import Counter
import re
import threading
import queue
import requests
from bs4 import BeautifulSoup
import click


@click.command(name="multithread_server")
@click.argument('n_threads')
@click.argument('top_k_frequent')
def multithread_server(n_threads, top_k_frequent):
    """Multithread server"""

    server = MyServer()
    server.start_multithread_server(n_threads, top_k_frequent)


class MyServer:
    """Server"""
    def __init__(self):
        self.jobs_finished = 0
        self.host = "127.0.0.1"
        self.port = 5004

    @staticmethod
    def beautifulsoup_extract_text_fallback(response_content):
        """Delete html tags"""
        if isinstance(response_content, str):
            soup = BeautifulSoup(response_content, 'html.parser')
        else:
            soup = BeautifulSoup(response_content.text, 'html.parser')
        text = soup.find_all(text=True)

        cleaned_text = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head',
            'input',
            'script',
            'style', ]

        for item in text:
            if item.parent.name not in blacklist:
                cleaned_text += f'{item} '

        cleaned_text = cleaned_text.replace('\t', '')
        return cleaned_text.strip()

    def get_most_common_word(self, url, top_k_frequent):
        """get_most_common_word"""
        # get text
        request = requests.get(url, timeout=60)
        # delete tags and make all words lowercase
        clean_text = self.beautifulsoup_extract_text_fallback(request).lower()
        # keep only letters and spaces
        letters_text = re.sub(r'[^a-zA-Zа-яА-Я ]', '', clean_text)
        # make list from text
        words_list = letters_text.split()
        # delete all one-symbol words
        words_list = list(filter(lambda word: len(word) > 2, words_list))
        # count most common words
        result = dict(Counter(words_list).most_common(top_k_frequent))
        return f"{url}: {result}"

    def communicate(self, connections_queue, top_k_frequent, thread_lock):
        """communicate"""
        while True:
            try:
                current_connection = connections_queue.get()
            except queue.Empty:
                continue

            current_url = current_connection.recv(1024)

            # If client sent death_pill_url to this thread
            if current_url.decode() == 'death_pill_url':
                current_connection.sendall('All urls are processed'.encode())
                current_connection.close()
                break

            data_str = self.get_most_common_word(current_url.decode(), top_k_frequent)
            current_connection.sendall(data_str.encode())
            current_connection.close()

            thread_lock.acquire()
            self.jobs_finished += 1
            print(f'Processed urls total amount: {self.jobs_finished}')
            thread_lock.release()

    def start_multithread_server(self, n_threads, top_k_frequent):
        """multithread_server"""
        program_lock = threading.Lock()
        top_k_most_frequent = int(top_k_frequent)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as active_socket:
            active_socket.bind((self.host, self.port))
            active_socket.listen()

            active_queue = queue.Queue()
            client_threads = [
                threading.Thread(
                    target=self.communicate,
                    args=(active_queue, top_k_most_frequent, program_lock)
                )
                for _ in range(int(n_threads))
            ]

            for thread in client_threads:
                thread.start()
            while True:
                active_connection = active_socket.accept()[0]
                active_queue.put(active_connection)


if __name__ == '__main__':
    multithread_server()  # pylint: disable=no-value-for-parameter
