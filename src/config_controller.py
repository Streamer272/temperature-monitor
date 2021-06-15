from json import loads


class ConfigController:
    logging_speed: int = 10

    @staticmethod
    def get_logging_speed():
        with open("config.json", "r") as file:
            try:
                return loads(file.read())["speed"]

            except KeyError:
                return ConfigController.logging_speed
