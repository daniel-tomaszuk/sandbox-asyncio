import asyncio
from typing import Any

from aioredis import create_redis


class OneAtATime:
    def __init__(self, redis, keys):
        self.redis = redis
        self.keys = keys

    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            k = next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration
        value = await self.redis.get(k)
        return value


async def main():
    redis = await create_redis(('localhost', 6379))
    keys = ['Americas', 'Africa', 'Europe', 'Asia']

    async for value in OneAtATime(redis, keys):
        await do_something_with(value)


async def do_something_with(stuff: Any):
    print(stuff)


if __name__ == "__main__":
    asyncio.run(main())
