import random

randomNum = random.randint(1, 10)
print(f"randomNum = {randomNum}")

# print("黑马儿童乐园，欢迎来游玩")
# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("您已成年，需要买票10元")
# else:
#     print("您未成年，可以免费游玩")
#
# print("祝您游玩愉快")
#
# if age > 20:
#     print("年龄大于20")
# else:
#     print("年龄小于20")

sum1 = 0
i = 1
while i <= 100:
    sum1 = sum1 + i
    i += 1

print(sum1)

# 这是一个猜数字的小游戏
# 随机一个数字，用来供猜想使用
target = random.randint(1, 100)
# 记录一共猜测了多少次
count = 0
# 标记循环条件
flag = True
# 开始循环
while flag:
    count += 1
    try:
        num = int(input("请输入你猜想的数字： "))
    except Exception as e:
        print(f"程序异常，异常原因是： {e}")
    if target == num:
        print("恭喜你，猜中了")
        flag = False
    else:
        if target > num:
            print("猜小了")
        else:
            print("猜大了")

print(f"一共猜测了： {count} 次")
