from gpiozero import CPUTemperature
from time import sleep
from src.logger import Logger
from src.config_controller import ConfigController


def run():
    cpu_temp = CPUTemperature()

    while True:
        temp = cpu_temp.temperature

        Logger.log(f"{temp}", Logger.INFO)

        sleep(ConfigController.get_logging_speed())


if __name__ == '__main__':
    run()
