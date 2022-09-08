import termcharts

chart = termcharts.bar(
    {"roll": 24, "bss": 10, "wes": 30, "ewfwef": 50}, title="Brunches"
)
print(chart)
chart = termcharts.bar(
    {
        "roll": 100,
        "bss": 40,
        "wes": 30,
        "ewfwef": 50,
        "ewsax": 50,
        "ewasx": 50,
        "ewasxaOOOf": 50,
    },
    title="Brunches",
    mode="v",
)
print(chart)
chart = termcharts.bar(
    [10, 20, 30, 40],
    title="Brunches",
    mode="v",
)
print(chart)
chart = termcharts.bar(
    [10, 20, 30, 40],
    title="Brunches",
    mode="h",
)
print(chart)
