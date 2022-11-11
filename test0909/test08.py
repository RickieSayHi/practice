"""
这是一个模拟发工资的小程序
"""
import random

total = 10050
salary = 1000
count = 0

for x in range(1, 21):
    point = random.randint(1, 10)
    if point < 5:
        print(f"员工 {x}, 绩效分 {point}， 低于5， 不发工资，下一位。")
        continue
    else:
        if total >= salary:
            total = total - salary
            print(f"向员工 {x} 发放工资 {salary} 元， 账户余额还剩余 {total} 元")
            count += 1
        else:
            if total > 0:
                print(f"向员工 {x} 发放工资 {total} 元， 账户余额还剩余 {total - total} 元")
                count += 1
            print(f"工资发完了，一共发放了 {count} 个员工的工资，下个月领取吧")
            break
