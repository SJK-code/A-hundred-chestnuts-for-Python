'''
Description: 得到左闭右开区间内所有偶数
Author: QiuYe
Date: 2022-07-15 22:22:36
LastEditors: QiuYe
LastEditTime: 2022-07-15 22:27:30
FilePath: \A hundred chestnuts for Python\7、计算数字范围内所有的偶数.py
'''
from turtle import begin_fill

def get_even_numbers(begin,end):
    result = []
    for i in range(begin, end):
        if i % 2 == 0:
            result.append(i)
    return result

if __name__ == "__main__":
    begin=4
    end =15
    print(f"begin = {begin},end = {end},all_even_numbers:", get_even_numbers(begin,end))
    