import os
from time import sleep
from threading import Thread
"""
Threading on MAC.
https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/CreatingThreads/CreatingThreads.html#//apple_ref/doc/uid/10000057i-CH15-SW7
https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091
"""

if __name__ == "__main__":

    threads = [
      Thread(target=lambda: sleep(10)) for i in range(10)
    ]

    [t.start() for t in threads]
    print(f'PID = {os.getpid()}')
    [t.join() for t in threads]
