#author:lpw
#date:
from  shopping.core import  login
import os
basedir= os.path.dirname(__file__)
file="%s\\user.txt" % basedir
replicefile="%s\\replicefile.txt" % basedir
fp = open(file,mode="r",encoding="utf-8")
fp2=open(replicefile,mode="a+",encoding="utf-8")
def chongzhi(login_status):
    for i in fp.readlines():
        if  login_status[0] in i :
            balance = int(i.rstrip("\n").split(":")[-1])
            number = input("请输入充值金额： ")
            totle = balance + int(number)
            fp2.writelines(login_status[0]+":"+login_status[1]+":"+str(totle)+"\n")
        else:
            fp2.writelines(i)
    fp.close()
    fp2.close()
    fp3 = open(file,mode="",encoding="utf-8")
    fp4=open(replicefile,mode="r",encoding="utf-8")
    for i in fp4.readlines():
        fp3.writelines(i)
    fp3.close()
    fp4.close()
if __name__ == '__main__':
    print("##########欢迎前来充值##########")
    # login_status=('www', 'www', '0', 1)
    login_status=login.login()
    print(login_status)
    chongzhi(login_status)