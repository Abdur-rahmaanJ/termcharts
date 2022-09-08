import math
from itertools import cycle

from termcharts.colors import Color
from termcharts.colors import default_colors
from termcharts.engine import add_char
from termcharts.engine import add_text
from termcharts.engine import merge_screens
from termcharts.engine import render
from termcharts.engine import screen
from termcharts.formula import constrain


def bar_chart_raw_h(data, title, return_rich=False):
    top_pad = 3
    right_pad = 2
    values_x = 500
    values_y = 100

    term_size_x = 40 + 1
    term_size_y = top_pad + len(data) + (len(data) - 1) + 2

    screen_axis = screen()
    screen_chart = screen()

    # Add left bar
    for i in range(term_size_x):
        add_char(screen_axis, [0, i + top_pad], Color.white + "│" + Color.RESET)

    max_item = max(data[e] for e in data)
    max_d_len = max(len(e) for e in data)

    # Draw bars
    space_pad = 1
    for i, item in enumerate(data):
        col = next(default_colors)
        width = term_size_x - (right_pad + max_d_len + 5)
        number = int(constrain(data[item], 0, max_item, 0, width))
        bar = f"{col}" + ("█" * number)

        if not return_rich:
            bar = bar + f" {data[item]}" + Color.RESET
        else:
            bar = bar + f" {data[item]}"
        add_text(screen_chart, bar, 1, top_pad + i + space_pad)
        space_pad += 1

    # Add title

    add_text(screen_chart, Color.white + title, 0, 1)

    main_screen = merge_screens([screen_chart, screen_axis])

    source = render(main_screen, term_size_x, term_size_y)

    if return_rich:
        try:
            from rich.text import Text
        except ImportError:
            raise Exception("Text not found from rich.text")
        return Text.from_ansi(source)
    else:
        return source


def bar_chart_raw_v(data, title, return_rich=False):
    top_pad = 4
    right_pad = 2
    values_x = 500
    values_y = 100
    bottom_pad = 1

    max_item = max(data[e] for e in data)
    max_d_len = max(len(e) for e in data)

    term_size_y = 15
    chart_size_x = len(data) + (len(data) - 1) + 2
    if title is None:
        term_size_x = chart_size_x
    elif title:
        if len(title) > chart_size_x:
            term_size_x = len(title) + 2
        else:
            term_size_x = chart_size_x + 5

    screen_axis = screen()
    screen_chart = screen()

    # Draw bars
    space_pad = 1

    for i, item in enumerate(data):
        # print(item)
        col = next(default_colors)
        height = term_size_y - (top_pad + bottom_pad)
        number = int(constrain(data[item], 0, max_item, 0, height))

        if not return_rich:
            bar = [f"{col}█{Color.RESET}" for i in range(number + 1)]
        else:
            bar = [f"{col}█" for i in range(number + 1)]
        txt_start_y = term_size_y - len(bar) - bottom_pad
        add_text(screen_chart, bar, i + space_pad, txt_start_y, mode="v")
        space_pad += 1

    # Add title
    add_text(screen_chart, Color.white + title, 0, 1)

    # Add bottom bar
    add_text(screen_axis, [f"{Color.white}─" * chart_size_x], 0, term_size_y - 1)

    # ---
    main_screen = merge_screens([screen_chart, screen_axis])

    source = render(main_screen, term_size_x, term_size_y)

    if return_rich:
        try:
            from rich.text import Text
        except ImportError:
            raise Exception("Text not found from rich.text")
        return Text.from_ansi(source)
    else:
        return source


def bar(data, title, rich=False, mode="h"):
    if mode == "h":
        return bar_chart_raw_h(data, title, return_rich=rich)
    if mode == "v":
        return bar_chart_raw_v(data, title, return_rich=rich)
