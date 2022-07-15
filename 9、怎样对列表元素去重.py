'''
Description: file content
Author: QiuYe
Date: 2022-07-15 22:45:04
LastEditors: QiuYe
LastEditTime: 2022-07-16 00:04:51
FilePath: \A hundred chestnuts for Python\9、怎样对列表元素去重.py
'''

import re
from unittest import result

'''错误示范'''
def match_repeating_elements(original_list):
    repeating_elements =[]
    temp = None
    for i in range(0,len(original_list)):
        temp = original_list[i]
        for j in range(0,len(original_list)):
            if i!=j & original_list[j] == temp:
                repeating_elements.append(temp)
    return repeating_elements

def match_remove_repeating(original_list):
    result = []
    for item in original_list:
        if item not in result:
            result.append(item)
    return result

def get_repeating_elements(original_list):
    unique_list = []
    repeating_elements =[]
    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)
        else:
            repeating_elements.append(item)
    return unique_list,repeating_elements
            
if __name__ == "__main__":
    origin_list = [2,4,4,5,5,6]
    print(f"1、原本列表：{origin_list},重复元素：{match_repeating_elements(origin_list)}") #错误示范！！！
    
    origin_list = [2,4,4,5,5,6]
    unique_list = match_remove_repeating(origin_list)
    print(f"2、原本列表：{origin_list},去重后的列表： {unique_list}")
    
    origin_list = [2,4,4,5,5,6]
    print(f"3、原本列表：{origin_list},去重后的列表： {list(set(origin_list))}")
    
    origin_list = [2,4,4,5,5,6]
    print(f"4、原本列表：{origin_list},去重后的列表： {get_repeating_elements(origin_list)[0]},重复的元素列表： {get_repeating_elements(origin_list)[1]}")
    