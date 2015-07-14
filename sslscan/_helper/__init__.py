from colorama import Fore
from colorama import init

init(autoreset=False)


def rating2color(color, level):
    # ToDo:
    if level is None:
        return color.RESET
    if level < 3:
        return color.OK
    if level < 5:
        return color.WARNING
    if level < 7:
        return color.DANGER
    return color.RESET


class ColorConsole(object):
    def __init__(self):
        #self.config = config

        self.colors = {
            "RESET": Fore.RESET,
            "BLACK": Fore.BLACK,
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "BLUE": Fore.BLUE,
            "MAGENTA": Fore.MAGENTA,
            "CYAN": Fore.CYAN
            # "GRAY": Fore.GRAY
        }

        self.mapped_colors = {}
        self.mapped_colors["default"] = {
            "DANGER": "RED",
            "ERROR": "RED",
            "OK": "GREEN",
            "SUCCESS": "GREEN",
            "WARNING": "YELLOW"
        }

    def __getattr__(self, name):
        #scheme = self.config.get_value("color")
        #if scheme == "none":
        #    return ""
        scheme = 'default'
        mapped_colors = self.mapped_colors.get(
            scheme,
            self.mapped_colors.get("default", {})
        )
        map_name = mapped_colors.get(name, "")
        if map_name != "":
            name = map_name
        code = self.colors.get(name, "")
        return code
