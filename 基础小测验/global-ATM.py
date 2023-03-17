'''
Description: file content
Author: QiuYe
Date: 2023-03-17 11:52:32
LastEditors: QiuYe
LastEditTime: 2023-03-17 11:56:20
FilePath: \A hundred chestnuts for Python\基础小测验\global-ATM.py
'''
def show_total_money():
    global total_money
    print(f"当前余额为{total_money}\n")


def save_money():
    global total_money
    try:
        num = eval(input("你要存多少钱？"))
        total_money += num
        print(f"你刚存入{num}元钱,", end='')
        show_total_money()
    except:
        print('输入有误！请输入数字！')
        save_money()


def withdraw_money():
    global total_money
    try:
        num = eval(input("你要取多少钱？"))
        if total_money < num:
            print("不好意思，当前余额不足！", end="")
        else:
            total_money -= num
            print(f"你刚取出{num}元钱,", end='')
        show_total_money()
    except:
        print('输入有误！请输入数字！')
        withdraw_money()


def option_action():
    global option
    option = input("请你选择当前业务：【0】查询余额【1】存钱 【2】取钱 【3】退出: ")


if __name__ == '__main__':
    print("欢迎使用ATM机!")
    total_money = 0
    option = 0
    while option != '3':
        option_action()
        if option == '0':
            show_total_money()
        elif option == "1":
            save_money()
        elif option == '2':
            withdraw_money()
        elif option == '3':
            print("您选择了退出ATM，欢迎下次继续使用！")
        else:
            print("您输入的选项有误，请重新选择！")
