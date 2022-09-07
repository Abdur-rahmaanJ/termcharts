# at coord we put symbol
# 0-0
import itertools
import math

from termcharts.colors import Color
from termcharts.colors import default_colors
from termcharts.engine import add_char
from termcharts.engine import coord_in_scr
from termcharts.engine import coord_to_str
from termcharts.engine import get_coord
from termcharts.engine import pie_add_text as add_text
from termcharts.engine import pie_render as render


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

        add_char(screen, [gx, gy], symbol)


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
    total = sum(data[d] for d in data)
    deg_current = 0
    # for i in range(10):

    if fill == True:
        fill_factor = 21
    else:
        fill_factor = 5

    max_d_len = sum(len(e) for e in data)
    for s, d in enumerate(data):

        deg_step = int((data[d] / total) * 360)
        col = next(default_colors)

        # legend
        # add_text(screen, col + d, 25, s + 2)
        # add_text(screen, 'x', 25, 3)
        # add_char(screen, [10, 3], '#')

        # print(col+d)
        # print(col+d)
        if not return_rich:
            txt = f"{col} {d} {Color.RESET}"
        else:
            txt = f"{col} {d}"

        # print(d, col+d, col+d+Color.RESET, file=open('z.log', 'w+'))

        # txt = d
        add_text(screen, txt, 25, s + 2)

        for i in range(10):

            if not return_rich:
                text = col + "█" + Color.RESET  # reset col
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

    display = 50 + max_d_len + 3

    source = render(screen, display - (25), display - (9 + max_d_len), debug=__debug)

    if return_rich:
        try:
            from rich.text import Text
        except ImportError:
            raise Exception("Text not found from rich.text")
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
