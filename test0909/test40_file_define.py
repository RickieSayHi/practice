"""
和文件相关的类定义
"""
# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
import json

from test40_data_define import Record


class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件的数据，读取到的每一条数据都转换成Record对象，将它们都封装到list内返回即可"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path            # 定义成员变量记录文件的路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        f = None
        try:
            f = open(self.path, "r", encoding="UTF-8")
            for line in f.readlines():
                line = line.strip()  # 消除读取到的每一行数据中的\n
                data_list = line.split(",")
                record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
                record_list.append(record)
        except Exception as e:
            print(f"程序异常，异常原因是： {e}")
        finally:
            if f:
                f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path            # 定义成员变量记录文件的路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        f = None
        try:
            f = open(self.path, "r", encoding="UTF-8")
            for line in f.readlines():
                line = line.strip()
                data_dict = json.loads(line)
                record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]),
                                data_dict["province"])
                record_list.append(record)
        except Exception as e:
            print(f"程序异常，异常原因是： {e}")
        finally:
            if f:
                f.close()
        return record_list


# 类文件方法测试
if __name__ == '__main__':
    text_file_reader = TextFileReader("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/2011年1月销售数据.txt")
    list1 = text_file_reader.read_data()

    json_file_reader = JsonFileReader("C:/CodeWorkingPlace/MyselfProjects/PycharmProjects/2011年2月销售数据.txt")
    list2 = json_file_reader.read_data()

    for x in list1:
        print(x)

    for y in list2:
        print(y)
