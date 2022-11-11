"""
练习嵌套循环打印 九九乘法表
"""

count = 0
i = 1
# 控制行的循环 i <= 9
while i <= 9:
    j = 1
    # 控制每行输出的循环 j <= i
    while j <= i:
        # 通过 \t 制表符对齐
        print(f"{j} * {i} = {i * j} \t", end="")
        j += 1
        count += 1
    # print() print空内容，就是输出一个空换行
    print("")
    i += 1
print(f"一共循环了 {count} 次")
