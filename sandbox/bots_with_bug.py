import threading
from enum import Enum
from queue import Queue

from attr import attrs, attrib

"""
Threading example with race condition bug (on purpose).
"""


class BotTaskEnum(str, Enum):
    prepare: str = "PREPARE TABLE"
    clean: str = "CLEAN TABLE"
    shutdown: str = "SHUTDOWN"


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()

    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == BotTaskEnum.prepare:
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == BotTaskEnum.clean:
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == BotTaskEnum.shutdown:
                return


@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)

    def give(self, to: "Cutlery", knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


if __name__ == "__main__":
    tables_to_serve = 50000
    kitchen = Cutlery(knives=100, forks=100)
    bots = [ThreadBot() for i in range(10)]
    for bot in bots:
        for _ in range(tables_to_serve):
            bot.tasks.put(BotTaskEnum.prepare)
            bot.tasks.put(BotTaskEnum.clean)
        bot.tasks.put(BotTaskEnum.shutdown)

    print('Kitchen inventory before service:', kitchen)
    for bot in bots:
        bot.start()

    for bot in bots:
        bot.join()
    print('Kitchen inventory after service:', kitchen)
