

async def f():
    return 123


if __name__ == "__main__":
    coro = f()
    try:
        coro.send(None)  # send None to the coroutine generator `x = yield`. async loop is doing it automatically
        # coro.throw(Exception, "boom")  # how to throw exception inside coroutine and cancel the task
    except StopIteration as e:
        print('The answer was:', e.value)
