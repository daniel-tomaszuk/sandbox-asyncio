import asyncio
from asyncio import Task


async def dummy_coroutine_source():
    pass


if __name__ == "__main__":
    """
    ensure_future ensures returned type, not that coro will be done.
    https://github.com/python/asyncio/issues/477#issuecomment-268709555
    """
    coroutine = dummy_coroutine_source()
    loop = asyncio.get_event_loop()

    task: Task = loop.create_task(coroutine)  # create and schedule Task (Future) -> class Task(Future)
    assert isinstance(task, asyncio.Task)

    new_task = asyncio.ensure_future(coroutine)  # creates task and schedule it to run
    assert isinstance(new_task, asyncio.Task)

    mystery_meat = asyncio.ensure_future(task)  # if ensure_future gets task - Task won't be changed as it's already a Future
    assert mystery_meat is task
