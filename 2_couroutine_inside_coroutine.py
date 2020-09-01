import asyncio


async def f():
    try:
        while True:
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        print('First Blood!')
        try:
            while True:
                await asyncio.sleep(0)
        except asyncio.CancelledError:
            print("Double Kill!")
    else:
        return 111


if __name__ == "__main__":
    """
    DONT DO THIS!
    """
    coro = f()
    coro.send(None)
    coro.throw(asyncio.CancelledError)
    coro.send(None)  # will be send into exception part
    coro.throw(asyncio.CancelledError)
