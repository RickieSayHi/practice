from test40_data_define import Record
from test40_file_define import FileReader, TextFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/2011年2月销售数据.txt")

text_data: list[Record] = text_file_reader.read_data()
json_data: list[Record] = json_file_reader.read_data()
# 将2个月份的数据合并为 1 个list来存储
all_data: list[Record] = text_data + json_data


# 开始进行数据计算

data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期已经有记录了，所以和老记录做累加即可
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 打印每一天的销售额
print(data_dict)

# 可视化图标开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))               # 添加 X 轴的数据
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))      # 添加 Y 轴的数据
bar.set_global_opts(
    title_opts=TitleOpts(title="2011年1月和2月 1号到10号的每日销售额"),
    xaxis_opts=AxisOpts(name_rotate=60, axislabel_opts={"rotate": 45}, name="日期"),      # 设置 x 轴坐标显示文本标签
    yaxis_opts=AxisOpts(name="各省每日销售额总和")                                           # 设置 y 轴坐标显示文本标签
)

bar.render("每日销售额柱状图.html")