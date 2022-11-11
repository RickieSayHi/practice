"""
时间线 的表格图
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})

# 创建柱状图对象
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国", "日本"])
bar1.add_yaxis("GDP", [30, 20, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国", "日本"])
bar2.add_yaxis("GDP", [50, 30, 40, 30], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国", "日本"])
bar3.add_yaxis("GDP", [80, 60, 50, 70], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

bar4 = Bar()
bar4.add_xaxis(["中国", "美国", "英国", "日本"])
bar4.add_yaxis("GDP", [100, 70, 80, 80], label_opts=LabelOpts(position="right"))
bar4.reversal_axis()

# 添加柱状图节点
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")
timeline.add(bar4, "点4")

# 设置时间线配置项， 自动播放等
timeline.add_schema(
    play_interval=2000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("GDP分析表时间线.html")