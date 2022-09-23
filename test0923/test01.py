"""
练习01
循环打印九九乘法表
"""


# 使用while循环打印

def func_while_print():
    count = 0
    i = 1
    while i <= 9:
        j = 1
        while j < i + 1:
            print(f"{j} * {i} = {j * i}\t", end="")
            j += 1
            count += 1
        print()
        i += 1
    print(f"一共循环了 {count} 次")


func_while_print()

print("\n")


# 使用for循环打印
def func_for_print():
    count = 0
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j} * {i} = {j * i}\t", end="")
            count += 1
        print()
    print(f"一共循环了 {count} 次")


func_for_print()
