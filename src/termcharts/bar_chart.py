from termcharts.engine import add_text
from termcharts.engine import render
from termcharts.engine import add_char
from termcharts.engine import screen
from termcharts.engine import merge_screens
from termcharts.colors import default_colors
from termcharts.formula import constrain

import math
from itertools import cycle

def bar_chart_raw(data, title, return_rich=False):
    RESET = '\033[39m'
    top_pad = 3
    right_pad = 2 
    values_x = 500
    values_y = 100

    term_size_x = 40 + 1
    term_size_y = top_pad + len(data) + (len(data)-1) + 2

    screen_axis = screen()
    screen_chart = screen()

    
    cols = cycle(default_colors)
    


    # Add left bar
    for i in range( term_size_x):
        add_char(screen_axis, [0, i+top_pad], '\033[37m│')

    max_item = max([data[e] for e in data])
    max_d_len = max([len(e) for e in data])
    # Draw bars
    space_pad = 1
    for i, item in enumerate(data):
        col = next(cols)
        width = term_size_x-(right_pad+max_d_len+5)
        number = int(constrain(data[item], 0, max_item, 0, width))
        bar = f'{col}'+('█'* number)

        if not return_rich:
            bar = bar + f' {data[item]}'
        else:
            bar = bar + f' {data[item]}' + RESET
        add_text(screen_chart, bar, 1, top_pad+i+space_pad)
        space_pad += 1

    # Add title

    add_text(screen_chart, '\033[37m'+title, 0, 1)

    
    main_screen = merge_screens([screen_chart, screen_axis])


    return render(main_screen, term_size_x, term_size_y)


def bar(data, title, rich=False):
    return bar_chart_raw(data, title, return_rich=rich)



