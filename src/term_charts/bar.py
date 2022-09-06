from term_charts.engine import add_text
from term_charts.engine import render
from term_charts.engine import add_char
from term_charts.engine import screen
from term_charts.engine import merge_screens
from term_charts.colors import default_colors
from term_charts.formula import constrain

import math
from itertools import cycle
RESET = '\033[39m'
def bar_chart_raw(data, title):
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
        bar = bar + f' {data[item]}'
        add_text(screen_chart, bar, 1, top_pad+i+space_pad)
        space_pad += 1

    # Add title

    add_text(screen_chart, '\033[37m'+title, 0, 1)

    
    main_screen = merge_screens([screen_chart, screen_axis])
    return render(main_screen, term_size_x, term_size_y) + RESET



