# 构建数据
data = {"1992": [
        ["美国", 123],
        ["中国", 88],
        ["英国", 112],
        ["日本", 108],
        ["德国", 109],
        ["印度", 40],
        ["俄罗斯", 110]
],
        "1994": [],
        "1996": [],
        "1998": [],
        "2000": [],
        "2002": [],
        "2004": [],
        "2006": [],
        "2008": [],
        "2010": []}


# 设置xyAxis示范
from pyecharts.charts import Line

x = ['2018-{:0>2d}'.format(s) for s in range(1, 13)]
y1 = [5, 10, 26, 30, 35, 30, 20, 26, 40, 46, 40, 50]
y2 = [8, 20, 24, 36, 40, 36, 40, 45, 50, 53, 48, 58]
line = Line(title="月销售总额", width=600, height=420)
line.add(name="商家A", x_axis=x, y_axis=y1)
line.add(name="商家B", x_axis=x,
         y_axis=y2,
         # #=====设置xyAxis=====
         yaxis_min=0, yaxis_max=100,
         # 设置y坐标轴刻度范围
         xaxis_name='月份', yaxis_name='销售额',
         # x轴名称，y轴名称
         xaxis_name_gap=40,
         # x轴名称与轴距离
         xaxis_rotate=30,
         # x轴刻度旋转角度
         is_splitline_show=True,
         # 显示y轴网格线
         is_xaxislabel_align=True
         # x轴刻度和标签是否对齐
         )

