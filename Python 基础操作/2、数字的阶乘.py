'''
Description: file content
Author: QiuYe
Date: 2022-07-15 19:17:24
LastEditors: QiuYe
LastEditTime: 2022-07-15 20:49:11
FilePath: \A hundred chestnuts for Python\2、数字的阶乘.py
'''

from ast import Str, Try
from math import fabs
from unittest import result 


def get_Factorial(number):
    result = 1
    list = []
    print("计算过程为：")
    while number >0:
        result *= number
        list.append(str(number))
        number -=1
    print('*'.join(list) +'=' + str(result))
    return result
    
if __name__ == "__main__":
                
    while True:
        b = input('输入一个正整数：')
        try:
            a = float(b)
            isBack = True
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
            isBack = False
            
        if isBack:
            if (a- int(a)) >0:
                print("请不要输入小数")
            elif ((float(a) - int(float(a))) <0)|(float(a) < 0):
                print("请不要输入负数")
            else:
                print("您输入的是正整数！")
                result = get_Factorial(int(a))
                print(f"得出{int(a)} 的阶乘是：{result}")
                break
