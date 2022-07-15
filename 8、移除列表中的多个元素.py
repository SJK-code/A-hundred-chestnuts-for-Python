'''
Description: file content
Author: QiuYe
Date: 2022-07-15 22:28:55
LastEditors: QiuYe
LastEditTime: 2022-07-16 00:38:03
FilePath: \A hundred chestnuts for Python\8、移除列表中的多个元素.py
'''

'''注意！！！ 自己想的思路解题有些复杂了'''
def remove_designed_number(origin_list,remove_list):
    for i in origin_list:
        for j in remove_list:
            if i == j:
                origin_list.remove(i)
    return origin_list

'''简单的！！！'''
def remove_designed_number_plus(origin_list,remove_list):
    for item in remove_list:
        origin_list.remove(item)
    return origin_list


if __name__ == "__main__":
    
    '''方法一：注意！！！ 自己想的思路解题有些复杂了''' 
    origin_list = [2,4,4,5,6,7,8,9,10,11,12,13]
    remove_list = [12,2]
    print(f"原本的列表:{origin_list}，移除{remove_list}后的列表：", remove_designed_number(origin_list,remove_list))
    
    '''方法二：简单的！！！'''
    origin_list = [2,4,4,5,6,7,8,9,10,11,12,13]
    remove_list = [12,2]
    print(f"原本的列表:{origin_list}，移除{remove_list}后的列表：", remove_designed_number_plus(origin_list,remove_list))
    
    '''方法三：还有内置方法·更简单'''
    origin_list = [2,4,4,5,6,7,8,9,10,11,12,13]
    remove_list = [4,2]
    data = [item for item in origin_list if item not in remove_list]
    print(f"原本的列表:{origin_list}，移除{remove_list}后的列表：", data)