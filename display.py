#conding:utf-8
#author:lpw
fp=open("msg.txt",mode="r",encoding="UTF-8")
for line in fp.readlines():
    a=line.split("*")
    print(a)

print("#"*30)
print(a)
fp.close()