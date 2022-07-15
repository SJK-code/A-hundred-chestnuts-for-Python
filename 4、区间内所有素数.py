'''
Description: 
# 素数定义是：如果一个数字只能被1和自己整除就是素数，否则不是素数
# 它除了能表示为它自己和1的乘积以外，不能表示为任何其它两个正整数的乘积
# 素数是在正整数范围内的研究，因此不能为负数。
Author: QiuYe
Date: 2022-07-15 21:03:38
LastEditors: QiuYe
LastEditTime: 2022-07-15 21:40:03
FilePath: \A hundred chestnuts for Python\4、区间内所有素数.py
'''
from cmath import inf
from math import fabs
from pydoc import doc
from tkinter.messagebox import RETRY

def print_primes(begin,end):
    
    for number in range(begin, end):
       if judge_prime(number):
            print(number,"是素数")
       elif number>0:
            print(number,"不是素数")
       
#函数：判断一个数是不是素数
def judge_prime(number):
    if  number <= 0:
        print(number,"不是正数")
        return False
    if  number == 2:
        return True
    if number == 1:
        print("1 既不是素数也不是质数")
    for i in range(2,number):
        if number%i == 0:
            return False
        elif number%1==0 & number%number ==0:
            return True

if __name__ == "__main__":
    #输入一个打印区间
    print_primes(-10,20)