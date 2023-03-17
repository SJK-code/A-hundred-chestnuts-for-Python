'''
Description: file content
Author: QiuYe
Date: 2022-07-15 20:55:49
LastEditors: QiuYe
LastEditTime: 2022-08-04 19:32:35
FilePath: \A hundred chestnuts for Python\3、求圆的面积.py
'''
from math import pi

def CalculateCircularArea(radius):
    if  radius < 0:
        print("半径有问题哦！")
        return radius
    return round(radius * radius * pi,2)

if __name__ == '__main__':
   print(CalculateCircularArea(2))