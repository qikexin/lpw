#author:lpw
#date:
'''
调用login.py返回元组结果如 （u_name,lock_status）
'''
# print("#########欢迎登陆购物网站##########")
import os
def login():
    num=1
    userlist=[]
    passwordlist=[]
    lock_user_list=[]
    basedir=os.path.dirname(__file__)
    # print(basedir)
    file1="%s\\user.txt" % basedir
    file2="%s\\lockuser.txt" % basedir
    file3="%s\\replicefile.txt" % basedir
    # file4="%s\\active.txt" % basedir

    # print(file1)
    lock_status=None # 1表示账号是活跃状态，可购买物品，0表示锁定状态，不能购买商品
    fp = open(file1,mode="r+",encoding="utf-8")
    fp2=open(file2,mode="a+",encoding="utf-8")
    fp3=open(file3,mode="r",encoding="utf-8")
    # fp4=open(file4,mode="",encoding="utf-8")
    print("#########欢迎登陆购物网站##########")
    for name in fp2.readlines():
            lock_user_list.append(name.rstrip("\n"))
    for i in fp.readlines():
            userlist.append(i.rstrip("\n").split(":")[0])
            passwordlist.append(i.rstrip("\n").split(":")[1])
    while True:
        u_name = input("请输入用户名： ")
        u_passwd= input("请输入密码： ")
        if  u_name in lock_user_list :
            lock_status = 0
            print("账号处于锁定状态，无法购买商品")
            return u_name,lock_status
            # exit(2)
        if u_name in userlist and u_passwd in passwordlist:
            print("登陆成功，可以开始购物")
            for newline in fp3.readlines():
                currtlins=newline.rstrip("\n").split(":")
                if u_name in currtlins:
                    print("用户 %s 的当前余额为: %s" % (u_name,currtlins[-1]))
            fp3.close()
            fp.close()
            lock_status = 1
            return  u_name,lock_status
            # exit(0)
        else:
            print("输入的账号或密码错误，请重新输入")
            num+=1
            if num < 4:
                continue
            else:
                print("账号被锁定，请联系管理员！")
                lock_status = 0
                fp2.writelines(u_name+"\n")
                fp2.close()
                return  u_name,lock_status
                # exit(3)

if __name__ == '__main__':
    login_status=login()
    status=login_status[-1]
    # print(status)