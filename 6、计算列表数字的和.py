'''
Description: file content
Author: QiuYe
Date: 2022-07-15 21:53:01
LastEditors: QiuYe
LastEditTime: 2022-07-15 22:20:55
FilePath: \A hundred chestnuts for Python\6、计算列表数字的和.py
'''
from unittest import result

from numpy import Inf, str_


if __name__ == "__main__":
    
    list = []
    while True:
        try:
            b = input("输入数,单独输入’#‘开始计算：")
            if b == "#":
                print("计算结果：")
                break
            a = float(b)
            isNumber = True
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
            isNumber = False
        
        if isNumber:
            list.append(a)
    
    str_list = []
    for line in list:
        str_list.append(str(line))
    print(" + ".join(str_list) + ' = ' + str(sum(list)))
        