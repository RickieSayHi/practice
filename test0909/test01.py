"""
这是一个演示
"""
"""
这是一个多行注释
"""
print(23411)
print(22323)
money = 50
print("钱包中还有： ", money)
money = money - 10
print("买冰淇淋话费10元，剩余： ", money, "元")
money = money - 5
print("买可乐花费5元，剩余： ", money, "元")

# 这是打印语句
print("零基础，学IT")
print("月薪过万")
print("就来黑马程序员")
print(45)
print(13.14)

print(type(444))
print(type(13.14))
print(type("四周"))

print("==================================")

num = 4
num += 1
print("num += 1 : ", num)
num -= 1
print("num -= 1 : ", num)
num *= 2
print("num *= 2 : ", num)
num /= 2
print("num /= 2 : ", num)
num %= 2
print("num %= 2 : ", num)
num = 9
num //= 2
print("num //= 2 : ", num)
num **= 2
print("num **= 2 : ", num)
num = num // 2
print("num //= 2 : ", num)

print("==================================")

# % 号占位符的形式
num1 = 11.34
num2 = 11.1235
print("11.34 取精度小数点后1位是： %.1f" % num1)
print("11.1235 取小数点后3位是： %.3f" % num2)

print("11.34 限制宽度为 7， 是： %7.1f" % num1)
print("11.1235 限制宽度为 8， 是： %8.2f" % num2)

name = "传智播客"
set_up_year = "2006"
price = 19.99

# 快速格式化输出打印方法
# f: format
print(f"{name}是在{set_up_year}年成立，每期学费价格为{price}元")

name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 30
print(f"公司是{name}，股票代码是{stock_code}，股票价格是 {stock_price}")
print("股票增长系数为 %.1f ， 经过 %2d 天增长， 股价达到了 %.2f" % (stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor ** 30))


result = input("请告诉我你是谁？")
print(f"我知道了，你是： {result}")