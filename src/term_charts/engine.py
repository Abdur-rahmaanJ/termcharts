from typing import Union

def coord_to_str(coord):
    return "-".join([str(i) for i in coord])


def add_char(screen: dict, coord: Union[list, tuple], value):
    # add coord to screen
    coord_str = coord_to_str(coord)
    screen[coord_str] = value


def get_coord(screen, coord: Union[list, tuple]):
    return screen[coord_to_str(coord)]


def coord_in_scr(screen: dict, coord: Union[list, tuple]):
    return coord_to_str(coord) in screen


def render(screen, displayx, displayy, debug=False):
    c = 0
    xxx = ""
    for x in range(displayx):
        for y in range(displayy):
            c += 1
            if c % (displayy) == 0:
                if debug:
                    end = "|\n"
                else:
                    end = "\n"
            else:
                end = ""

            if not coord_in_scr(screen, [x, y]):
                xxx = xxx + " " + end
            else:
                xxx = xxx + get_coord(screen, [x, y]) + end

    return xxx


def add_text(screen, text, gx, gy, mode='h'):
    x = 0
    y = 0
    for c in text:
        if mode == 'h':
            add_char(screen, [gy, gx + x], c)
            x += 1
        if mode == 'v':
            add_char(screen, [gy+y, x], c)
            y += 1


def screen():
    return {}
from collections import ChainMap

def merge_screens(screens):
    screens = reversed(screens)
    return dict(ChainMap(*screens))