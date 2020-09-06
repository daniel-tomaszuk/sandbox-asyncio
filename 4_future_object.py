import asyncio


async def main(future: asyncio.Future, time: int):
    await asyncio.sleep(time)
    print(f'Done: {time}')
    future.set_result('I have finished.')


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    fut1 = asyncio.Future()
    fut2 = asyncio.Future()

    print(fut1.done())  # not done
    print(fut2.done())  # not done

    loop.create_task(main(fut1, 5))  # schedule, but not run yet
    loop.create_task(main(fut2, 6))  # schedule, but not run yet
    loop.run_until_complete(fut2)

    print(fut1.done())  # done
    print(fut2.done())  # done
    print(fut1.result())  # gets result
    print(fut2.result())  # gets result
