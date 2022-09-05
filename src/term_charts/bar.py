from term_charts.engine import add_text
from term_charts.engine import render
from term_charts.engine import add_char
from term_charts.engine import screen
from term_charts.engine import merge_screens

import math

def bar_chart_raw():
	screen_axis = screen()
	screen_chart = screen()

	

	for x in range (0, 500):
		m = 4
		c = 0
		# y = m * x + c

		k = 10
		n = 10


		v = math.sin(math.radians(x)) 
		# for t in range(0, 360):
		
		y = 10 + abs(v)* 50

		# y = x**2 - 5

		# y = k * x ** 1.1

		gx = int(x//5)
		gy = int(y//5)

		print(x, y, gx, gy)
		add_char(screen_chart, [gy, gx], '*')

	add_text(screen_axis,'the lazy fox jumps over the quick dog', 0, 0)
	add_text(screen_axis,'the lazy fox jumps over the quick dog', 0, 0, mode='v')
	
	main_screen = merge_screens([screen_chart, screen_axis])
	return render(main_screen, 100, 100)



