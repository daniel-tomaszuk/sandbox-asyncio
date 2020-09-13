import asyncio


async def plus_100(x):
    await asyncio.sleep(0.1)
    return x + 100


async def factory(n):
    for x in range(n):
        await asyncio.sleep(0.1)
        yield plus_100, x


async def main():
    results = [await f(x) async for f, x in factory(10)]
    print('results = ', results)


if __name__ == "__main__":
    asyncio.run(main())
