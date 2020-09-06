import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def web_page(url):  
    loop = asyncio.get_event_loop()
    # use `run_in_executor` for blocking functions, don't forget about `await` keyword befor!
    data = await loop.run_in_executor(
        None, download_webpage, url)  
    yield data
    await loop.run_in_executor(None, update_stats, url)  

async with web_page('google.com') as data:
    process(data)
