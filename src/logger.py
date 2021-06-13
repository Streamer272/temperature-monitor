from datetime import datetime, date


class Logger:
    INFO = 0
    WARNING = 1
    ERROR = 2

    @staticmethod
    def get_level_name_by_level(level: int):
        level_names = ["INFO", "WARNING", "ERROR"]

        return level_names[level]

    @staticmethod
    def log(message, level: int = 0, console=True, file=True):
        formatted_message = f"{Logger.get_level_name_by_level(level)} {datetime.now()}: {message}"

        if console:
            print(formatted_message)

        if file:
            with open(f"./log/log-{date.today()}.log", "a") as file:
                file.write(f"{formatted_message}\n")
