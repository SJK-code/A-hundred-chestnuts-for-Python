# 数据存储仓库
stu_list = [
    {'id': 1, 'name': '岳岳1', 'tel': '1234561'},
    {'id': 2, 'name': '岳岳2', 'tel': '1234562'},
    {'id': 3, 'name': '岳岳3', 'tel': '1234563'},
    {'id': 4, 'name': '岳岳4', 'tel': '1234564'},
    {'id': 5, 'name': '岳岳4', 'tel': '1234564'}
]

"""显示功能界面"""


def welcome():
    print("""
========欢迎进入学生管理系统,请选择你要实现的功能========
            ********1、添加学员信息********
            ********2、删除学员信息********
            ********3、修改学员信息********
            ********4、查找学员信息********
            ********5、退出当前系统********""")  # 注释文档的作用  不改变我们原有的格式


"""获取用户输入的菜单编号"""


def get_choose_number():
    choose_number = input('请输入你的菜单编号:')  # 6
    # 判断你输入的字符串时候为数字
    # 如果编号不是数字 或者 不是['1','2','3','4','5'] 中的一个
    # 满足证明我输入是有错误的
    if not choose_number.isdigit() or choose_number not in ['1', '2', '3', '4', '5']:
        return -1  # 标识
    return int(choose_number)  # 后面的函数调用


"""主函数"""


def main():
    # 死循环
    while True:
        welcome()
        number = get_choose_number()
        # 在函数外面使用到函数内部的值  ------》retrun
        if number == -1:
            print('编号输入有误请重新输出！！！')
            # 希望我的循环结束嘛
            continue  # 跳过输出错误的一次 不影响我后面的循环

        if number == 1:
            add_stu()
        elif number == 2:
            del_stu()
        elif number == 3:
            set_stu()
        elif number == 4:
            find_stu()
        else:
            break


"""定义添加学员函数"""


def add_stu():
    flag = True
    while flag:
        new_id = int(input('请输入学号:'))
        new_name = input('请输入姓名:')
        new_tel = input('请输入手机号:')
        # 存到列表中 并且每一个学员的格式为字典

        # 临时的字典存储
        dict_data = {}
        dict_data['id'] = new_id  # 字典中没有这个键  相当与添加
        dict_data['name'] = new_name  # 字典中没有这个键  相当与添加
        dict_data['tel'] = new_tel  # 字典中没有这个键  相当与添加
        # print(dict_data)   # 放到列表中
        # 解决重复的问题 判断
        if dict_data in stu_list:
            print('该学员已经被添加过了！！！')
        else:
            stu_list.append(dict_data)
            print('该同学已经被添加进列表了！')
            add_next = input('是否继续添加(1、添加2、返回系统首页)')
            if add_next == '2':
                flag = False
    print(stu_list)


"""定义删除学员函数"""


# 根据id去进行删除
def del_stu():
    flag = True
    while flag:
        stu_id = int(input('请输入你要删除学员的id:'))
        for data in stu_list:  # data 每一条学员信息
            if stu_id == data['id']:
                stu_list.remove(data)
                print('该学员信息已经被删除了！')
                break
        else:
            print('该学员不存在,请重新输入!')
        del_next = input('是否继续删除(1、删除2、返回系统首页)')
        if del_next == '2':
            flag = False
    print(stu_list)


"""定义修改学员函数"""


def set_stu():
    flag = True
    while flag:
        stu_id = int(input('请输入你要修改的学员的id:'))
        for data in stu_list:
            if stu_id == data['id']:
                data['id'] = int(input('请输入修改后的id:'))
                data['name'] = input('请输入修改后的姓名:')
                data['tel'] = input('请输入修改后的手机号:')
                print('该学员信息已经成功修改！！')
                break
        else:
            print('该学员不存在,请重新输入!!!')
        set_next = input('是否继续修改(1、修改2、返回系统首页)')
        if set_next == '2':
            flag = False
    print(stu_list)


"""
else语法解决的问题是：一般for循环结束后，我们无法直接知道for循环是提前跳出的，还是走完整个循环结束的，需要通过额外的if语句进行判断
"""

"""定义查找学员函数"""


def find_stu():
    while True:
        stu_info = input("请输入需要查找的学生任意一项信息：")
        if stu_info:
            result = [x for x in stu_list if stu_info in (*x.values(), str(x['id']))]
            if not result:
                print("查无此人")
            else:
                print(f"查找到 {len(result)} 位学生，学生信息分别为：")
                [print(f'学号：{stu["id"]} 姓名：{stu["name"]} 手机号:{stu["tel"]}') for stu in result]
            set_next = input('\n是否继续查询(1、查询 2、返回系统首页)')
            if set_next == '2':
                break
        else:
            print("输入不可为空！")
            continue


# 程序的主入口
if __name__ == '__main__':  # 程序的入口 只能有一个
    """知道我们程序的调用顺序"""
    main()
