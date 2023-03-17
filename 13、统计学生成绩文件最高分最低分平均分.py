'''
Description: file content
Author: QiuYe
Date: 2022-07-20 00:35:18
LastEditors: QiuYe
LastEditTime: 2022-08-05 19:46:10
FilePath: \A hundred chestnuts for Python\13、统计学生成绩文件最高分最低分平均分.py
'''

def main():
    nums = [1,1,0,0,0,0,1,1,1]
    count =0
    count1 =0
    count0 =0
    for i in range(len(nums)):
        x = nums[i]
        if x == 1:
            if count0 <= count1:
                count =0
            else:
                count +=1
            count0 +=1
        elif x == 0:
            if count0 >= count1:
                count =0
            else:
                count +=1
            count1 +=1
    print(count)

if __name__ == "__main__":
    main()