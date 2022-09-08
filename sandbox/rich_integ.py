from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from termcharts import bar
from termcharts import doughnut
from termcharts import pie

console = Console()


charts = [
    doughnut({"a": 10, "b": 20, "c": 30, "d": 20}, title="aphabet dist", rich=True),
    pie({"wefwefqwddwqdqwda": 10, "b": 20, "c": 30, "d": 20}, rich=True),
    bar({"roll": 24, "bss": 10, "wes": 30, "ewfwef": 50}, title="Brunches", rich=True),
    bar({"a": 23, "b": 23, "c": 23, "d": 60}, title="Brunches", rich=True, mode="v"),
]
user_renderables = [Panel(x, expand=True) for x in charts]
# print(user_renderables)
console.print(Columns(user_renderables))
