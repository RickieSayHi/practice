"""
基础地图的使用
"""

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [
    ("北京", 99),
    ("上海", 199),
    ("安徽", 299),
    ("江苏", 399),
    ("湖南", 499),
    ("山西", 599)
]

map.add("测试地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FFF666"},
            {"min": 100, "max": 199, "label": "100-199", "color": "#CC5555"},
            {"min": 200, "max": 499, "label": "200-499", "color": "#AA223E"},
            {"min": 500, "max": 999, "label": "500-999", "color": "#CBBF5F"},
        ]
    )
)

map.render()