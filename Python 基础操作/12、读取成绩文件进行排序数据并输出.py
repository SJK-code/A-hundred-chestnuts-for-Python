'''
Description: file content
Author: QiuYe
Date: 2022-07-20 00:12:23
LastEditors: QiuYe
LastEditTime: 2022-07-20 00:33:16
FilePath: \A hundred chestnuts for Python\12、读取成绩文件进行排序数据并输出.py
'''

import encodings
from numpy import e


def read_file(filename):
    result = []
    filename = "./数据文件/" + filename
    with open(filename, "r",encoding="utf-8") as f_input:
        for line in f_input:
            line = line[:-1]
            result.append(line.split(","))
        return result

def sortStudentDatas(data, isReverse):
    return sorted(data, key=lambda x: int(x[2]),reverse=isReverse)

#输入文件：三列：学号、姓名、成绩
#数据格式：列于列直之间用逗号隔开，比如：101,小刘,68
#行与行之间的用换行符\n进行分割
# 处理文件，按照成绩进行倒叙排序
# 如何读取文件
if __name__ == "__main__":
    result = read_file("student_input.txt")
    print(result)
    
    result_sorted = sortStudentDatas(result,True)
    print(result_sorted)
    
    #写入文件
    with open("student_input_sorted.txt", "w", encoding="utf-8") as f:
        for data in result_sorted:
            f.write(', '.join(data) + "\n")