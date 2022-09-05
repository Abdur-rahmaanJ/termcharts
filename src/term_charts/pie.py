from typing import Union

# at coord we put symbol
# 0-0
import math
import itertools

screen = {}

def coord_to_str(coord):
    return '-'.join([str(i) for i in coord])

def add_c(scr: dict, coord: Union[list, tuple], value):
    # add coord to screen
    coord_str = coord_to_str(coord)
    screen[coord_str] = value


def get_c(screen, coord: Union[list, tuple]):
    return screen[coord_to_str(coord)]

def coord_in_scr(screen: dict, coord: Union[list, tuple]):
    return coord_to_str(coord) in screen


def render(screen, displayx, displayy, debug=False):
    c = 0
    xxx = ''
    for x in range(displayx):
        for y in range(displayy):
            c += 1
            if c%(displayy ) == 0:
                if debug:
                    end = '|\n'
                else:
                    end = '\n'
            else:
                end = ''

            if not coord_in_scr(screen, [x, y]):
                xxx = xxx+ ' '+ end
            else:
                xxx = xxx+ get_c(screen, [x, y]) +end


    return xxx


# def y_right(x, r, xc, yc):
#     return yc+math.sqrt(r**2 - ((x-xc)**2))


def corx(xc, r, theta):
    return xc + (r * math.cos(math.radians(theta)))
def cory(yc, r, theta):
    return yc + (r * math.sin(math.radians(theta)))


# for i in range(10):
#     print(y_right(i, 30, 30, 30))


# grid size 80 * 80
# coord to grid:

grid_s = 20
centerx = 270
centery = 250
rx = 200
ry = 200


def add_text(screen, text, gx, gy):
    x = 0
    for c in text:
        
        add_c(screen, [gy, gx+x], c)
        x +=1

def sector_line(centerx, centery, rx, ry, degstart, degend, grid_s, screen, symbol):
    for i in range(degstart, degend):
        x = corx(centerx, rx, i)
        y = cory(centery, ry, i)

        gx = int(x//grid_s)
        gy = int(y//grid_s)

        add_c(screen, [gx, gy], symbol)


def pie_chart_raw(data: dict, centerx, centery, rx, ry, grid_s, screen, return_rich=False, __debug=False, fill=False):
    pie_cols = itertools.cycle(['\033[31m', '\033[32m', '\033[33m', '\033[35m'])
    total = sum([data[d] for d in data])
    deg_current = 0
    # for i in range(10):

    if fill==False:
        fill_factor = 10
    else:
        fill_factor = 21
    for s, d in enumerate(data):
        
        deg_step = int((data[d]/total)*360)
        col = next(pie_cols)

        # legend
        add_text(screen, col+d, 25, s+2)
        for i in range(10):

            if not return_rich:
                text = col + '█\033[39m' # reset col
            else: 
                text = col + '█'
            sector_line(centerx, centery, rx-(i*fill_factor), ry-(i*fill_factor), deg_current, deg_current+deg_step, grid_s, screen, text)
        deg_current += deg_step


    add_text(screen, 'pie chart', 0, 1)


    display = 45

    source = render(screen, display-15, display, debug=__debug)



    if return_rich:
        return Text.from_ansi(source)
    else:
        return source



def pie_chart(data, return_rich=False):
    global centerx, centery, rx, ry, grid_s, screen
    fill = True
    return pie_chart_raw(data, centerx, centery, rx, ry, grid_s, screen, fill=fill, return_rich=return_rich)



def doughnut_chart(data, return_rich=False):
    global centerx, centery, rx, ry, grid_s, screen
    fill = False
    return pie_chart_raw(data, centerx, centery, rx, ry, grid_s, screen, fill=fill, return_rich=return_rich)
