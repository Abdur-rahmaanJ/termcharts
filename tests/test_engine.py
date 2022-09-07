import sys
import pytest
sys.path.append('.')
from src.termcharts.engine import merge_screens
from src.termcharts.engine import coord_in_scr
from src.termcharts.engine import pie_add_text
from src.termcharts.engine import coord_to_str
from src.termcharts.engine import pie_render
from src.termcharts.engine import get_coord
from src.termcharts.engine import add_text
from src.termcharts.engine import add_char
from src.termcharts.engine import render


"""
Pytest docs:
    - https://docs.pytest.org/en/7.1.x/
Testing module for termcharts/engine.py
Each function has it's own `screen` localized and tested separately
"""

def test_coord_to_str():
    output = coord_to_str('testing')
    expected = 't-e-s-t-i-n-g'
    assert output == expected, '`coord_to_str()` function may be changed but test not updated'


def test_render():
    screen = {"0-0": "x", "10-20": "@"}
    add_char(screen, [0, 3], "/")

    string = render(screen, 11, 21)
    assert (
        string.replace(" ", "+").replace("\n", "<br>")
        == "x++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>/++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++++<br>++++++++++++++++++++@<br>"
    )


def test_coord_in_scr():
    screen = {}
    screen['10-10'] = 'test'
    
    assert not coord_in_scr(screen, [12, 10]), "`coord_in_scr()` reports false positive"
    assert coord_in_scr(screen, [10, 10]), "`coord_in_scr()` reports false negative"


def test_pie_add_text():
    screen = {}
    pie_add_text(screen, 'test', 4, 4, mode='h')
    expexted = {
        '4-4': 't',
        '4-5': 'e',
        '4-6': 's',
        '4-7': 't',
    }
    assert screen == expexted, "`pie_add_text()` failes at `horizontal` mode"

    screen.clear()

    pie_add_text(screen, 'test', 4, 4, mode='v')
    expexted = {
        '4-0': 't',
        '5-0': 'e',
        '6-0': 's',
        '7-0': 't',
    }
    assert screen == expexted, "`pie_add_text()` failes at `vertical` mode"


def test_add_text():
    screen = {}
    add_text(screen, 'test', 4, 4, mode='h')
    expected = {
        '4-4': 't',
        '5-4': 'e',
        '6-4': 's',
        '7-4': 't',
    }
    assert screen == expected, "`add_text()` failes at `horizontal` mode"

    screen.clear()

    add_text(screen, 'test', 4, 4, mode='v')
    expected = {
        '0-4': 't',
        '0-5': 'e',
        '0-6': 's',
        '0-7': 't',
    }
    assert screen == expected, "`add_text()` failes at `vertical` mode"


def test_get_coord():
    screen = {'10-5': 'test'}
    assert get_coord(screen, [10, 5]) == screen['10-5']


def test_merge_screens():
    screen1 = {"10-5": "1", "10-6": "2"}
    screen2 = {"8-3": "A", "9-3": "B"}
    screens = [screen1, screen2]

    merged = merge_screens(screens)
    expected = {
        "10-5": "1",
        "10-6": "2",
        "8-3": "A",
        "9-3": "B",
    }

    assert merged == expected
