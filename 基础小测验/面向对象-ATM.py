class ATM():
    def __init__(self, total_money):
        self.total_money = total_money

    def show_blance(self):
        print(f"当前余额为：{self.total_money}")


class save_withdraw_money(ATM):
    def __init__(self, total_money=0, save_money=0, withdraw_money=0):
        super().__init__(total_money)
        self.save_money = save_money
        self.withdraw_money = withdraw_money

    def save_action(self):
        self.save_money = eval(input("你想存入多少钱？"))
        self.total_money += self.save_money
        print(f"刚存入{self.save_money}元")

    def withdraw_action(self):
        self.withdraw_money = eval(input("你想取出多少钱？"))
        if self.withdraw_money > self.total_money:
            print(f"余额不足，当前余额为{self.total_money}")
        else:
            self.total_money -= self.withdraw_money
            print(f"刚取出{self.withdraw_money}元")


if __name__ == '__main__':
    vocational_work = save_withdraw_money()
    while True:
        option = input("【0】查询【1】存钱 【2】取钱 【3】退出: ")
        if option == '0':
            vocational_work.show_blance()
        elif option == '1':
            vocational_work.save_action()
        elif option == '2':
            vocational_work.withdraw_action()
        elif option == '3':
            print("欢迎下次使用！")
            break
        else:
            print("您输入的选项有误！")
