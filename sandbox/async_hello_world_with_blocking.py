import asyncio, time


async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1)
    print(f'{time.ctime()} Goodbye!')


async def main2():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(10)
    print(f'{time.ctime()} Goodbye!')


def blocking():
    # blocking tme must be less or equal to the live time of async loop
    time.sleep(5)
    print(f"{time.ctime()} Hello from a thread!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    task2 = loop.create_task(main2())
    task3 = loop.create_task(main())

    loop.run_in_executor(None, blocking)

    loop.run_until_complete(task)
    loop.run_until_complete(task2)
    loop.run_until_complete(task3)

    # try me:
    # blocking()

    pending = asyncio.all_tasks(loop=loop)
    for task in pending:
        task.cancel()
    group = asyncio.gather(*pending, return_exceptions=True)

    # loop lives until last task returns from it. If executors are still alive, error will be thrown.
    loop.run_until_complete(group)
    loop.close()
