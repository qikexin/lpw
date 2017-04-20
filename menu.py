#conding:utf-8
#author:lpw
import  sys

menu='''
======菜单项======
1、购买商品
2、查询消费记录
3、显示余额
4、充值
'''
tag=True
while tag:
    num_menu=input("请输入1/2/3/4/q: ")
    if num_menu.isdigit():
        num_menu = int(num_menu)
        if num_menu == 1:
            print("购买商品")
            import shopping
        elif num_menu == 2:
            print("查询消费记录")
        elif num_menu == 3:
            print("显示余额")
        elif num_menu == 4:
            print("充值")
        else :
            print("输入错误,退出")
            tag = False
    elif num_menu == "q":
        print("退出")
        tag = False
    else:
        print("输入错误")
        tag = False

