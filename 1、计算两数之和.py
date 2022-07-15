'''
Description: file content
Author: QiuYe
Date: 2022-06-28 20:47:31
LastEditors: QiuYe
LastEditTime: 2022-07-15 20:49:17
FilePath: \A hundred chestnuts for Python\1、计算两数之和.py
'''

'''Description: 计算两个数字之和'''
from ast import Try
from keyword import issoftkeyword
from numpy import true_divide

if __name__ == "__main__":

    while True:
        try:
            a = float(input("输入第一个数："))
            break
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
            
    while True:
        try:
            b = float(input("输入第二个数："))
            break
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
    c =a+b;   
    print(f"{a}+{b}={c}")