#author:lpw
#date:
#coding=utf-8
import sys
import time
import  user_login

menu='''
======菜单项======
1、购买商品
2、查询消费记录
3、显示余额
4、充值
'''
#print(menu)
goods={
    1:["手机",1250],
    2:["电视",3400],
    3:["笔记本",5300],
    4:["电子书",120],
    5:["面包",15],
    6:["书包",120],
    7:["鞋子",200],
    8:["上衣",120],
    9:["裤子",100],
    10:["手套",20]
}
#判断登录账号是否被锁定，如果被锁定不能购买商品
fp_lock = open("lock.txt",mode="r",encoding="utf8")
line = fp_lock.readline()
a=line.split(",")
if user_login.aaaaaaaaa in a:
    print("your name is locked，please get help from admin")
    sys.exit(8)
#购买商品
welcome_msg = "welcome to lpw shopping"
salary = input("input your salary:")
#输出欢迎信息，入户用户信息，如薪水，此处扩展可以是用户登录后记录下用户名
if salary.isdigit():
    salary = int(salary)
    print("your salary is :",salary)
    print(welcome_msg.center(50,"-"))
    # print(goods)
else:
    exit("invalid data type")

msg = []  #用来记录用户信息和购买物品信息
          #如果需要用户信息可以在此处list.append(用户私有信息，如用户名)
          #也可以将之后所有物品话费的zongjia追加到此list中，list,append(zongjia)
list = []  #获取goods中商品名和单价
for value in goods.values():
    list.append(value)
# print(list)
#这里循环是为了输出商品名称和价格做准备
i=1  #定义一个初始化计数器
j=0  #定义一个初始化计数器
for key in goods.keys():
    print(i,":",list[j][0],"  单价:",list[j][1])  #输出的是所有的商品id号和商品名
    i+=1
    j+=1

#id=input("input the 1/2/3/... to select :") #输入要购买的商品id号
wupin=[] #将用户所选商品添加到列表中
zongjia=0 #记录用户所选所有商品的总价的初始值
tag=True
while tag:
    id=input("input the 1/2/3/... to select :") #输入要购买的商品id号
    if id.isdigit():
        id = int(id)
        # wupin.append(list[id-1][0])
        print(id,":",list[id-1][0])  #打印商品id和商品名
        number=input("购买数量: ")
        if number.isdigit():
            number=int(number)
            # wupin.append(number)
            #此处计算余额，余额不足退出购物
            # print("your salary is :",salary)
            rest = salary - list[id-1][1]*number
            # print(rest)
            if rest > 0:
                wupin.append(list[id-1][0])
                zongjia+=list[id-1][1]*number
                # print(zongjia)
                CONTINUE_1=input("继续购买输入:y,去结算输入:n **** ")
                if CONTINUE_1 == "y":
                    continue
                else:
                    tag=False
                    break
            else:
                print("余额不足")
                #pass  #退出购买过程，去结算
                tag=False
                sys.exit(8)
        else:
            continue


#打印所选商品，并记录入文件中
print("购买的商品包括:%s" % wupin)
print("所有商品的总价为:%d元" % zongjia)
#结算过程,输出剩余的钱
print("剩余%d元" % rest)
#以下将用户的登录信息和购买记录信息记录到文件中
#msg.append("*")
msg.append(user_login.aaaaaaaaa)
msg.append(wupin)
msg.append(number)
time=time.strftime('%Y%m%d-%H:%M:%S',time.localtime(time.time()))
msg.append(time)
msg.append(rest)
print(msg)
xinxi='''
------------用户购买信息-----------
用户名: %s
商品: %s
数量：%d
日期: %s
余额: %d
''' % (msg[0],msg[1],msg[2],msg[3],int(msg[4]))
print(xinxi) #打印购买信息并记录到文件中
fp = open("msg.txt",mode="a+",encoding="UTF-8")
string=str(msg)
#fp.write(string)
fp.writelines(string)
fp.write("*")
#fp.write("\r\n")
fp.close()
#查询消费记录
#显示余额





