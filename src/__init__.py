import random

from gpiozero import CPUTemperature
from time import sleep
from src.logger import Logger
from src.graph import Graph


def run():
    win = Graph()

    while True:
        win.hide_graph()

        # temp = CPUTemperature().temperature
        temp = random.randint(10, 90)

        Logger.log(f"{temp}", Logger.INFO)

        win.add(temp)
        win.update_data()
        win.show_graph()

        sleep(.5)


if __name__ == '__main__':
    run()
