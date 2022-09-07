import itertools

# if need instantiation use dataclass
class Color:
    RESET = "\033[39m"

    red = "\033[31m"
    green = "\033[32m"
    orange = "\033[33m"
    purple = "\033[35m"
    white = "\033[37m"


default_colors = itertools.cycle([Color.red, Color.green, Color.orange, Color.purple])
