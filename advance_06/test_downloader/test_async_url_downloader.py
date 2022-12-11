import pytest
from asyncmock import AsyncMock
import async_url_downloading


@pytest.mark.asyncio
async def test_process_urls():
    async_url_downloading.fetch_url = AsyncMock(return_value='request mock')
    with open('test_output.txt', 'w') as output:
        output.truncate()
    await async_url_downloading.process_urls(10, 'test_urls.txt', 'test_output.txt')

    with open('test_output.txt', 'r') as input_file:
        info = input_file.read()
        assert info == 'request mock\n' * 2
