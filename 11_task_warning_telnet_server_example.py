import asyncio
from asyncio import StreamReader, StreamWriter

SERVER_ADDRESS = "0.0.0.0"
SERVER_PORT = 8000


async def main(host: str = SERVER_ADDRESS, port: int = SERVER_PORT):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


async def echo(reader: StreamReader, writer: StreamWriter):
    """
    Reader and Writer are passed from `asyncio.start_server`.
    """
    print('New connection.')
    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()
        print('Leaving Connection.')
    except asyncio.CancelledError:
        # Will be thrown if there are still running tasks while server is closed.
        message = "Connection dropped!"
        print(message)
        # BUG !
        # As a general rule of thumb, try to avoid creating new tasks inside CancelledError exception handlers.
        # If you must, be sure to also await the new task or future inside the scope of the same function.
        asyncio.create_task(send_log_event_mock(message))


async def send_log_event_mock(message: str):
    await asyncio.sleep(1)


if __name__ == "__main__":
    print("Starting the Server!")
    print(f"Use `telnet {SERVER_ADDRESS} {SERVER_PORT}` command to connect with the server.")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye!')
