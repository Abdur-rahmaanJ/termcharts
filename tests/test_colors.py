from termcharts.colors import Color


def test_colors():
    assert Color.red == "\033[31m"
