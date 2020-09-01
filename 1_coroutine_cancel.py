import asyncio


async def f():
    times_fired = 0
    try:
        while True:
            print(f'Do The Coroutine! Fire!: {times_fired}')
            times_fired += 1
            await asyncio.sleep(0)

    except asyncio.CancelledError:
        print('I was cancelled!')
    else:
        return 111


if __name__ == "__main__":
    coro = f()
    # fire the coroutine
    coro.send(None)
    coro.send(None)
    coro.send(None)
    coro.throw(asyncio.CancelledError)
