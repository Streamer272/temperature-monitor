from json import loads


class ConfigController:
    @staticmethod
    def get_logging_speed():
        with open("config.json", "r") as file:
            try:
                return loads(file.read())["speed"]

            except KeyError:
                return 10
