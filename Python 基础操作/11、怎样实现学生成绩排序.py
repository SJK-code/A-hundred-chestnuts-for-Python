'''
Description: 学习使用lambda 表达式进行排序
Author: QiuYe
Date: 2022-07-20 00:00:42
LastEditors: QiuYe
LastEditTime: 2022-07-20 00:11:03
FilePath: \A hundred chestnuts for Python\11、怎样实现学生成绩排序.py
'''
# 使用 复杂列表，元素是属于字典或者元组 进行排序

def StudentSort():
    
    pass

if __name__ == "__main__":
    #声明一个元组 或者 数组
    students = [
        {"sno":101,"sname": "小张","sgrade":88},
        {"sno":102,"sname": "小王","sgrade":75},
        {"sno":103,"sname": "小李","sgrade":97},
        {"sno":104,"sname": "小赵","sgrade":68}
        # {"sno":105,"sname": "小刘","sgrade":68},
    ]
    students_sort = sorted(students, key = lambda x: x["sgrade"],reverse = True)
    print(f"source{students},\nsort result: {students_sort}")
