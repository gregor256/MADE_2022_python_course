from unittest import mock
from server import get_most_common_word


def test_most_common_word():
    with open('simple_http.txt', 'r') as http_example:
        with mock.patch("requests.get") as requests_get:
            requests_get.return_value = http_example.read()
            result = get_most_common_word('https://www.example.com', 1)
            assert result == "https://www.example.com: {'domain': 4}"
