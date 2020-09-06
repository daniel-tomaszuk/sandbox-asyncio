from contextlib import asynccontextmanager
from contextlib import contextmanager


class Connection:
    """
    Example of async context manager - aenter, aexit mothods are required
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def __aenter__(self):
        self.conn = await self.get_conn(self.host, self.port)
        return self.conn

    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()

    async def get_conn(self, host, port):
        # do something
        return object


@contextmanager
def web_page(url):
    # Sync context manager with decorator
    data = download_webpage(url)  
    yield data
    update_stats(url)  


@asynccontextmanager  
async def web_page_async(url):
    # Async context manager with decorator
    data = await download_webpage(url)  
    yield data  
    await update_stats(url)  


if __name__ == "__main__":
    async with Connection('localhost', 9001) as conn:
        pass

    with web_page('google.com') as data:
        process(data)

    async with web_page_async('google.com') as data:
        process(data)
