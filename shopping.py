#author:lpw
#date:
#author:lpw
#date:
#coding=utf-8
import sys
import  user_login
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
#goods定义了商品信息
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
list = []  #获取goods中商品名和单价的中间值
for value in goods.values():
    list.append(value)
# print(list)
#这里循环是为了输出商品名称和价格做准备
i=1  #定义一个初始化计数器
j=0  #定义一个初始化计数器
for key in goods.keys():
    print(i,":",list[j][0])  #输出的是所有的商品id号和商品名
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
        #此处计算余额，余额不足退出购物
        # print("your salary is :",salary)
        rest = salary - list[id-1][1]
        # print(rest)
        if rest > 0:
            wupin.append(list[id-1][0])
            zongjia+=list[id-1][1]
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


#打印所选商品，并记录入文件中
print("购买的商品包括:%s" % wupin)
print("所有商品的总价为:%d元" % zongjia)

#结算过程,输出剩余的钱
print("剩余%d元" % rest)
#以下将用户的登录信息和购买记录信息记录到文件中
msg.append(user_login.aaaaaaaaa)
msg.append(wupin)
msg.append(rest)
print("记录用户的购买记录%s" % msg)

fp = open("D:\\test\\test\\msg.txt",mode="a+",encoding="utf8")
string=str(msg)
fp.write(string)
fp.write("\r\n")
fp.close()






