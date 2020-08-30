import asyncio, time


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


if __name__ == "__main__":
    # black box way:
    # asyncio.run(main())

    # verbose way
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())

    all_tasks = asyncio.all_tasks(loop=loop)

    loop.run_until_complete(task)

    pending = asyncio.all_tasks(loop=loop)
    for task in pending:
        task.cancel()

    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()
