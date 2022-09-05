from typing import Union
from collections import ChainMap

def coord_to_str(coord):
    r = "-".join([str(i) for i in coord])
    return r


def add_char(screen: dict, coord: Union[list, tuple], value):
    # add coord to screen
    coord_str = coord_to_str(coord)

    print(coord_str, value)
    screen[coord_str] = value


def get_coord(screen, coord: Union[list, tuple]):
    return screen[coord_to_str(coord)]


def coord_in_scr(screen: dict, coord: Union[list, tuple]):
    return coord_to_str(coord) in screen


def render(screen, size_x, size_y, debug=False):
    string = ''
    end = ''
    counter = 0

    for y in range(size_y):
        for x in range(size_x):
            counter += 1
            if counter % size_x == 0:
                end = '\n'
            else:
                end = ''

            coord = f'{x}-{y}'
            if coord not in screen:
                string = string + '  ' + end
            else:
                string = string + screen[coord] + end

    

    return string


def add_text(screen, text, gx, gy, mode='h'):
    x = 0
    y = 0

    

    for c in text:
        if 'h' in mode:
            add_char(screen, [gy, gx + x], c)
            x += 1
        if 'v' in mode:
            add_char(screen, [gy+y, x], c)
            y += 1


def screen():
    return {}


def merge_screens(screens):
    screens = reversed(screens)
    return dict(ChainMap(*screens))