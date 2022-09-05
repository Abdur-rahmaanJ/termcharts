# download-stats

View your pypi download stats

# cli


```
$ download-stats shopyo
```

![](https://github.com/Abdur-RahmaanJ/download-stats/raw/stable/assets/download_stats.png)

```
$ download-stats --compare flask django fastapi
```

![](https://github.com/Abdur-RahmaanJ/download-stats/raw/stable/assets/compare.png)


```
$ download-stats --self # same as `download-stats download-stats`
```

## general

```python
>>> from download_stats import stats 
>>> stats('shopyo')
{
    "total": "41327",
    "30_days": "1484",
    "7_days": "506",
    "by_version": [
        ["Date", "4.5.7", "4.5.8", "4.6.0", "Sum", "Total"],
        ["2022-09-01", "0", "1", "3", "4", "24"],
        ["2022-08-31", "2", "1", "17", "20", "126"],
        ...
        ["2022-06-04", "0", "0", "0", "0", "9"],
    ],
}
```

## recent

```python
>>> from download_stats import recent                                                                          
>>> recent('shopyo') 
{
    "data": {"last_day": 23, "last_month": 454, "last_week": 142},
    "package": "shopyo",
    "type": "recent_downloads",
}
```

## version

```python
>>> from download_stats import version
>>> version('shopyo')
{
    "data": [
        {"category": "3", "date": "2022-03-06", "downloads": 1},
        ...
        {"category": "null", "date": "2022-08-31", "downloads": 55},
    ],
    "package": "shopyo",
    "type": "python_major_downloads",
}
>>> version('shopyo', version=3.9)
{
    "data": [
        {"category": "3.9", "date": "2022-03-12", "downloads": 1},
        {"category": "3.9", "date": "2022-03-18", "downloads": 15},
        ...
        {"category": "3.9", "date": "2022-08-29", "downloads": 2},
    ],
    "package": "shopyo",
    "type": "python_minor_downloads",
}
```

## system

```python
>>> from download_stats import system
>>> system('shopyo')
{
    "data": [
        {"category": "Darwin", "date": "2022-03-21", "downloads": 1},
        ...
        {"category": "Windows", "date": "2022-08-22", "downloads": 2},
    ],
    "package": "shopyo",
    "type": "system_downloads",
}
>>> system('shopyo', name='linux')
{
    "data": [
        {"category": "Linux", "date": "2022-03-08", "downloads": 1},
        ...
        {"category": "Linux", "date": "2022-08-31", "downloads": 3},
    ],
    "package": "shopyo",
    "type": "system_downloads",
}

```