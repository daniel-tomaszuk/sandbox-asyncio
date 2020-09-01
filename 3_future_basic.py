from asyncio import Future

if __name__ == "__main__":
    """
    A Future instance may also do the following:
    Have a “result” value set (use .set_result(value) to set it and .result() to obtain it)
    Be cancelled with .cancel() (and check for cancellation with .cancelled())
    Have additional callback functions added that will be run when the future completes
    """

    f = Future()
    print(f.done())
