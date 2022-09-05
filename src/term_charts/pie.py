import math
import itertools
from term_charts.engine import coord_to_str
from term_charts.engine import add_coord
from term_charts.engine import get_coord
from term_charts.engine import coord_in_scr
from term_charts.engine import render
from term_charts.engine import add_text



def corx(xc, r, theta):
    return xc + (r * math.cos(math.radians(theta)))


def cory(yc, r, theta):
    return yc + (r * math.sin(math.radians(theta)))


grid_s = 20
centerx = 250
centery = 250
rx = 200
ry = 200


def sector_line(centerx, centery, rx, ry, degstart, degend, grid_s, screen, symbol):
    for i in range(degstart, degend):
        x = corx(centerx, rx, i)
        y = cory(centery, ry, i)

        gx = int(x // grid_s)
        gy = int(y // grid_s)

        add_coord(screen, [gx, gy], symbol)


def pie_chart_raw(
    data: dict,
    centerx,
    centery,
    rx,
    ry,
    grid_s,
    screen,
    return_rich=False,
    __debug=False,
    fill=False,
    title="pie chart",
):
    pie_cols = itertools.cycle(["\033[31m", "\033[32m", "\033[33m", "\033[35m"])
    total = sum([data[d] for d in data])
    deg_current = 0
    # for i in range(10):

    if fill == True:
        fill_factor = 21
    else:
        fill_factor = 5

    for s, d in enumerate(data):

        deg_step = int((data[d] / total) * 360)
        col = next(pie_cols)

        # legend
        add_text(screen, col + d, 25, s + 2)
        for i in range(10):

            if not return_rich:
                text = col + "█\033[39m"  # reset col
            else:
                text = col + "█"
            sector_line(
                centerx,
                centery,
                rx - (i * fill_factor),
                ry - (i * fill_factor),
                deg_current,
                deg_current + deg_step,
                grid_s,
                screen,
                text,
            )
        deg_current += deg_step

    add_text(screen, title, 0, 1)

    display = 45

    source = render(screen, display - 20, display, debug=__debug)

    if return_rich:
        from rich.text import Text
        return Text.from_ansi(source)
    else:
        return source


def pie_chart(data, rich=False, title="pie chart", screen=None):
    global centerx, centery, rx, ry, grid_s
    fill = True
    if screen is None:
        screen = {}
    return pie_chart_raw(
        data,
        centerx,
        centery,
        rx,
        ry,
        grid_s,
        screen,
        fill=fill,
        return_rich=rich,
        title=title,
    )


def doughnut_chart(data, rich=False, title="doughnut chart", screen=None):
    global centerx, centery, rx, ry, grid_s
    fill = False
    if screen is None:
        screen = {}
    return pie_chart_raw(
        data,
        centerx,
        centery,
        rx,
        ry,
        grid_s,
        screen,
        fill=fill,
        return_rich=rich,
        title=title,
    )
