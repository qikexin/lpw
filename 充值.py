#coding="utf8"
#author:lpw
#date:

a=[]
fp = open("msg.txt",mode="r",encoding="UTF-8")
for line in fp.readlines():
    #print(type(line))
    a=line.split("*")
    print(type(a))
    print(a)

fp.close()