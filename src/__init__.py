import random

from gpiozero import CPUTemperature
from time import sleep
from src.logger import Logger
from src.config_controller import ConfigController


def run():
    while True:
        # temp = CPUTemperature().temperature
        temp = random.randint(10, 90)

        Logger.log(f"{temp}", Logger.INFO)

        sleep(ConfigController.get_logging_speed())


if __name__ == '__main__':
    run()
