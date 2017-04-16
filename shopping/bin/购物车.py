#author:lpw
#date:
from shopping.core import login
from shopping.core import zhuce
from shopping.core import addmoney
# import os
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))

print("1：新用户注册 2：登录 3: 充值")
n=input("请输入： ")
if int(n) == 1:
    zhuce_status= zhuce.zhuce()
elif int(n) == 2:
    login_status= login.login()
    print(login_status)
    print("$"*10)
elif int(n) == 3:
    addmoney.chongzhi()

else:
    print("输入错误！程序退出，请重新启动程序")





