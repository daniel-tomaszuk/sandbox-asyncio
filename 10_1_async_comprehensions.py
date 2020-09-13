import asyncio
import collections


async def power(n) -> collections.AsyncIterable:
    for i in range(n):
        yield i, i * i
        await asyncio.sleep(0.1)


async def main():
    # async list comprehension
    result = [x async for x in power(10)]
    print(result)

    # async dict comprehension
    result = {x: y async for x, y in power(10)}
    print(result)

    # async set comprehension
    result = {x async for x in power(10)}
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
