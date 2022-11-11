"""
异常的捕获
"""

def func1():
    print("func1 开始执行")
    res = 1 / 0
    print("func1 结束执行")

def func2():
    print("func2 开始执行")
    func1()
    print("func2 结束执行")

def main():
    print("main 开始执行")
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常信息为： {e}")
    print("main 结束执行")


main()