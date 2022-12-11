# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import pytest
from asyncmock import AsyncMock
import advance_06.fetcher


@pytest.mark.asyncio
async def test_process_urls():
    advance_06.fetcher.fetch_url = AsyncMock(return_value='request mock')
    with open('test_output.txt', 'w', encoding='utf-8') as output:
        output.truncate()
    await advance_06.fetcher.process_urls(10, 'test_urls.txt', 'test_output.txt')

    with open('test_output.txt', 'r', encoding='utf-8') as input_file:
        info = input_file.read()
        assert info == 'request mock\n' * 2
