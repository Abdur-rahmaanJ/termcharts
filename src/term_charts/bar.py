from term_charts.engine import add_text
from term_charts.engine import render




def bar_chart_raw():
	screen = {}
	add_text(screen,'the lazy fox jumps over the quick dog', 0, 0)
	add_text(screen,'the lazy fox jumps over the quick dog', 0, 0, mode='v')
	return render(screen, 20, 20)



