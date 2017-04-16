#author:lpw
#date:
'''
调用zhuce.py返回结果元组格式如   (用户名,密码,余额,注册状态)
新用户注册成功后写入uset.txt，格式如   用户名：密码：余额
'''

import os
def zhuce():
    print("##########欢迎注册用户##########")
    basedir=os.path.dirname(__file__)
    file1="%s\\user.txt" % basedir
    fp = open(file1,mode="a+",encoding="utf-8")
    u_name = input("请输入用户名：")
    balance=str(0) #表示余额
    while True:
        u_passwd =  input("请输入密码: ")
        u2_passw = input("请再次输入密码: ")
        if u_passwd == u2_passw:
            print("恭喜，注册成功！")
            fp.writelines(u_name+":"+u_passwd+":"+balance+"\n")
            zhuce_status=1
            return u_name,u_passwd,balance,zhuce_status
            fp.close()
            # exit(0)
        else:
            print("两次输入的密码不一致，请重新输入。")
            continue

if __name__ == '__main__':
    a=zhuce()
    print(a)
