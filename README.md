# termcharts

Terminal charts with rich compatibility in mind


![](https://github.com/Abdur-RahmaanJ/termcharts/raw/stable/assets/pie.png)

# bar

![](https://github.com/Abdur-RahmaanJ/termcharts/raw/stable/assets/bar.png)


```python
import termcharts


chart = termcharts.bar({'roll': 24, 'bread':10, 'rice':30, 'pasta':50}, title='brunches')
print(chart)
```

# pie

```python
import termcharts


chart = termcharts.pie({'pencil':10, 'eraser': 20, 'ruler': 30}, title='stationary')
print(chart)
```

# doughnut

```python
import termcharts


chart = termcharts.doughnut({'a':10, 'b': 20, 'c': 30}, title='aphabet dist')
print(chart)
```


# Rich compatibility


```python
from termcharts import pie
from termcharts import doughnut
from termcharts import bar

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

console = Console()

charts = [
    doughnut({'a':10, 'b': 20, 'c': 30, 'd': 20}, title='aphabet dist', rich=True), 
    pie({'wefwefqwddwqdqwda':10, 'b': 20, 'c': 30, 'd': 20}, rich=True),
    bar({'roll': 24, 'bss':10, 'wes':30, 'ewfwef':50}, title='Brunches', rich=True)
    ]
user_renderables = [Panel(x, expand=True) for x in charts]
console.print(Columns(user_renderables))
```


# Testing

All testing is currently handled by the [pytest](https://docs.pytest.org/en/7.1.x/) module and are incomplete at the momment.

Installation:
```
pip install -U pytest
```

Run all the testcases in a file:
```
pytest tests/<file>.py
```

Run one testcase in a file:
```
pytest tests/<file>.py::<function_name>
```

Exclude one testcase in a file:
```
pytest tests/<file>.py -k 'not <function_name>'
```
