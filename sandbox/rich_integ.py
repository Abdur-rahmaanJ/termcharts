from term_charts import pie
from term_charts import doughnut




from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel




console = Console()


charts = [
	doughnut({'a':10, 'b': 20, 'c': 30, 'd': 20}, title='aphabet dist', rich=True), 
	pie({'wefwefqwddwqdqwda':10, 'b': 20, 'c': 30, 'd': 20}, rich=True)]
user_renderables = [Panel(x, expand=True) for x in charts]
# print(user_renderables)
console.print(Columns(user_renderables))
