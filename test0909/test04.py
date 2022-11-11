"""
练习嵌套循环
"""

i = 1
while i <= 100:
    print(f"今天是第 {i} 天， 开始向小美表白")

    j = 1
    while j <= 10:
        print(f"给小美送第 {j} 朵玫瑰花")
        j += 1

    print("小美，我爱你")
    i += 1

print(f"坚持到第 {i - 1} 天， 表白成功")