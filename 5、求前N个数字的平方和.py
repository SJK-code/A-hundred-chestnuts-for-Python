'''
Description: 求取两个数字之间的平方和
#写两个函数，一个求平方、一个求和
Author: QiuYe
Date: 2022-07-15 21:41:05
LastEditors: QiuYe
LastEditTime: 2022-07-15 22:01:02
FilePath: \A hundred chestnuts for Python\5、求前N个数字的平方和.py
'''

from unittest import result

def adder(begin,end):
    result = 0
    list = []
    for i in range(begin, end+1):
        list.append(str(i))
        result += square(i)
    print("² + ".join(list) + '² = ' + str(result))

def square(number):
    return number * number

if __name__ == "__main__":
    adder(1,10)