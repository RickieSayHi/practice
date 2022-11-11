"""
综合案例： 黑马 ATM
"""

money = 5000000
name = input("您好，欢迎使用黑马银行ATM，请输入您的用户名： ")


def query(show_header):
    if show_header:
        print("==============【查询余额】================")
    print(f"{name}，您的账户里面还剩余额 {money} 元")


def save_money():
    print("==============【存款】================")
    num = int(input(f"{name}，您好，请输入你要存款的金额："))
    global money
    money += num
    print(f"存入 {num} 元成功，账户剩余存款为： {money} 元")
    query(False)


def get_money():
    print("==============【取款】================")
    num = int(input(f"{name}，您好，请输入你要取款的金额："))
    global money
    money -= num
    print(f"从账户中取出 {num} 元成功， 账户剩余存款为： {money} 元")
    query(False)


def main():
    print("==============【主菜单】================")
    print(f"欢迎您，{name}，请选择您想要办理的业务：")
    print("1.查询余额 \t[输入1]")
    print("2.存款 \t\t[输入2]")
    print("3.取款 \t\t[输入3]")
    print("4.退出 \t\t[输入4]")
    return int(input("请输入业务编号: "))


while True:
    step = main()
    if step == 1:
        query(True)
        continue
    elif step == 2:
        save_money()
        continue
    elif step == 3:
        get_money()
        continue
    else:
        print("程序结束，退出")
        break
