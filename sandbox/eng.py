from termcharts.engine import render
from termcharts.engine import add_char



screen = {
    '0-0': 'x',
    '10-20': '@'
}



print(render(screen, 11, 21))



add_char(screen, [0, 3], '/')


print(render(screen, 11, 21))
