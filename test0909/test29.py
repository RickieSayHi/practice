"""
基础柱状图的构建
"""

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

bar.add_xaxis(["中国", "美国", "英国"])

# 反转 x 和 y 轴 后，label_opts=LabelOpts(position="right")， 使数据显示在右侧
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# 反转 x 和 y 轴
bar.reversal_axis()

bar.render("GDP分析表.html")
