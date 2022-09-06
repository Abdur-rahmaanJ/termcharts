from typing import Union
from collections import ChainMap

def coord_to_str(coord):
    r = "-".join([str(i) for i in coord])
    return r


def add_char(screen_: dict, coord: Union[list, tuple], value):
    # add coord to screen
    coord_str = coord_to_str(coord)


    screen_[coord_str] = value


def get_coord(screen, coord: Union[list, tuple]):
    return screen[coord_to_str(coord)]


def coord_in_scr(screen: dict, coord: Union[list, tuple]):
    return coord_to_str(coord) in screen


def pie_render(screen, displayx, displayy, debug=False):
    displayx, displayy = displayy, displayx

    c = 0
    xxx = ""
    for x in range(displayx-20):
        for y in range(displayy):
            c += 1
            if c % (displayy) == 0:
                if debug:
                    end = "|\n"
                else:
                    end = "\n"
            else:
                end = ""


            if (x <= displayx and y <= displayy):
                # print(x, y, displayx, displayy)
                if not coord_in_scr(screen, [x, y]):
                    xxx = xxx + " " + end
                else:
                    xxx = xxx + get_coord(screen, [x, y]) + end

    return xxx

def render(screen, size_x, size_y):
    RESET = '\033[39m'
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

            if (x <= size_x and y <= size_y):
                if coord not in screen:
                    string = string + '  ' + end
                else:
                    string = string + screen[coord] + end

    
    return string

def pie_add_text(screen_, text, gx, gy, mode='h'):
    x = 0
    y = 0

    

    for c in text:
        if 'h' in mode:
            add_char(screen_, [gy, gx + x], c)
            x += 1
        if 'v' in mode:
            add_char(screen_, [gy+y, x], c)
            y += 1


def add_text(screen_, text, gx, gy, mode='h'):
    x = 0
    y = 0

    

    for c in text:
        if 'h' in mode:
            add_char(screen_, [gx + x, gy], c)
            x += 1
        if 'v' in mode:
            add_char(screen_, [x, gy+y], c)
            y += 1

def screen():
    return {}


def merge_screens(screens):
    screens = reversed(screens)
    return dict(ChainMap(*screens))