from term_charts.engine import add_text
from term_charts.engine import render
from term_charts.engine import add_char
from term_charts.engine import screen
from term_charts.engine import merge_screens
from term_charts.colors import default_colors
from term_charts.formula import constrain

import math
from itertools import cycle

def bar_chart_raw():
	
	values_x = 500
	values_y = 100

	term_size_x = 100
	term_size_y = 40

	screen_axis = screen()
	screen_chart = screen()

	
	cols = cycle(default_colors)
	col = next(cols)
	for x in range (0, values_x):
		m = 4
		c = 0
		# y = m * x + c

		k = 10
		n = 10


		v = math.sin(math.radians(x)) 
		# for t in range(0, 360):
		
		y = 10 + v* 50

		# y = x**2 - 5

		# y = k * x ** 1.1

		try:
			gx = int(constrain(x, 0, values_x, 0, term_size_x, lessthan_sym='', morethan_sym=''))
			gy = int(constrain(y, 0, values_y, 0, term_size_y, lessthan_sym='', morethan_sym=''))

			gy = term_size_y - gy
			# print(x, y, gx, gy)

			gx = gx + 5
			gy = gy - 5
			add_char(screen_chart, [gy, gx], col+'*\033[39m')
		except:
			pass

	# add_text(screen_axis,'the lazy fox jumps over the quick dog', 0, 0)
	# add_text(screen_axis,'the lazy fox jumps over the quick dog', 0, 0, mode='v')

	# add_text(screen_axis, '-'*term_size_x, 0, 0, mode='hi', term_size_x=term_size_x, term_size_y=term_size_y)
	# add_text(screen_axis, '+'+'|'*(term_size_y-1), 0, 0, mode='vi', term_size_x=term_size_x, term_size_y=term_size_y)


	x_axis = '+' + '-'*(term_size_x-1)

	# for x, char in enumerate(x_axis):
	#    add_char(screen_axis, [term_size_x-1, x], char)

	for x in range(term_size_x):
		add_char(screen_axis, [term_size_y-1, x], '─')

	add_text(screen_axis, '│'*(term_size_y-1)+'└', 0, 0, mode='v')

	
	main_screen = merge_screens([screen_chart, screen_axis])
	return render(main_screen, term_size_x, term_size_y)



