"""
JSON 数据的转换
"""

# 导入JSON模块
import json

# 准备JSON格式要求的Python数据
data = [{"name": "小明", "age": 18}, {"name": "小军", "age": 19}]
print(f"原始数据：  {data}")
print(type(data))

# 通过 json.dumps(data) 方法将 python 数据转化为了json数据
json_str = json.dumps(data, ensure_ascii=False)
print(f"数据 1 ： {json_str}")
print(type(json_str))

# 通过 json.loads(data) 方法将 json 数据转化为了 Python 数据
s = '[{"name": "明明", "age": 18}, {"name": "君君", "age": 19}]'
python_str = json.loads(s)
print(f"数据 2： {python_str}")
print(type(python_str))
