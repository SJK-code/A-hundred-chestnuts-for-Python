'''
Description: file content
Author: QiuYe
Date: 2022-07-16 00:06:50
LastEditors: QiuYe
LastEditTime: 2022-07-16 00:37:19
FilePath: \A hundred chestnuts for Python\10、怎样对简单列表元素排序.py
'''
# 对简单列表进行排序，并不是复合列表
# 用到了自带的排序函数 sort \ sorted 以及其参数 reverse

if __name__ == '__main__':
    original_list = [2,14,31,13,4,7,4]
    # 此时 original_list 本身已经改变
    original_list.sort(reverse = False)
    print(f"正序排序后的列表：{original_list}")
    original_list.sort(reverse = True)
    print(f"倒序排序后的列表：{original_list}")
    
    print("------------=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--------------")
    
    # 如何不改变原始的列表，而重新得到一个排好序的简单列表呢?
    original_list = [2,14,31,13,4,7,4]
    original_listb =[]
    original_listb = sorted(original_list)
    print(f"原始列表：{original_list}\n正序排序后的另外一个列表：{original_listb}\n再次打印原始列表{original_list}")