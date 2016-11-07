import  sys

#菜单-------
str =  '''
1、注册
2、登录
'''
print(str)
#-----------
state = 0
def zhuce ():
    tag = True
    txt = {}
    name = []
    fp = open("message.txt",mode="a+",encoding="utf8")
    fr = open("message.txt",mode="r",encoding="utf8")
    while tag:
        u_name = input("input your name: ")
 #19-26 注册时输入用户名后判断此用户是否已经注册
        for line in fr.readlines():
            line=line.rstrip('\n').rstrip('\r')
            a=line.split(":")
            name.append(a[0])
        if u_name in name:
            print("your name is exist")
            sys.exit(8)
#28--如果用户没有注册就执行注册新用户
        else:
            u_password = input("input your password: ")
            save = input("save or not , input y or n : ")
            if save == "y":
                txt[u_name]=u_password
                key=txt[u_name]
                vlue=txt.get(u_name)
                fp.writelines(key+":"+vlue)
                fp.write("\n")
                select = input("continue or exit,please input y or n :")
                if select == "y":
                    state = 1
                    return state
                    tag= False
                    break
                else:
                    print("注册成功，退出！")
                    sys.exit(8)
                    # state = 0
                    # tag = False
                    # break
            elif save == "n":
                tag = False
                state =2
                return state
                break
            else:
                print("input error,please run it again")
                tag =False
        fp.close()



def denglu():
    tag = True
    fpr = open("message.txt",mode="r",encoding="utf8")
    name = []
    password = []
    u_name = input("input your name : ")
#57-63用户登录时输入用户名后先判断用户名是否已锁定
    fp_lock = open("lock.txt",mode="r",encoding="utf8")
    line = fp_lock.readline()
    a=line.split(",")
    if u_name in a:
        print("your name is locked，please get help from admin")
        sys.exit(8)
    else:
        for line in fpr.readlines():
            line=line.rstrip('\n').rstrip('\r')
            a=line.split(":")
            name.append(a[0])
            password.append(a[1])
        #print("name is : ",name)
        #print("password is : ",password)
        #print(name.index("aaa"))
        #print(password[name.index("aaa")])
        #判断用户名是否存在
        while tag:
            #aaaaaaaaa=""
            if u_name in name:
                p_word = input("input your password : ")
                for i in range(3):
                    if password[name.index(u_name)] == p_word:
                        print("登录成功!! is ",u_name,p_word) #提示登录成功
                        tag = False
                        #aaaaaaaaa=u_name
                        return u_name
                        break
                    else:
                        if i == 2:
                            print("账号被锁定")   #85-90 用户输错3次密码后将锁定用户名
                            fp_lock = open("lock.txt",mode="a",encoding="utf8")
                            fp_lock.writelines(u_name + ",")
                            fp_lock.close()
                            tag = False
                            return(u_name)
                            break
                        else:
                            p_word=input("reinput password : ")
                            continue
            else:
                tag = False
                print("账号不存在")
                continue
        fpr.close()
        #return  u_name

num = input("input a number : ")
if num.isdigit():
    num = int(num)
    if num == 1:
        print("1、注册")
        state = zhuce()
        if state == 1:
            print("请登录！")
            aaaaaaaaa=denglu()
            print(aaaaaaaaa)
        else:
            print("注册失败")
    elif num == 2:
        print("2、登录")
        aaaaaaaaa=denglu()
        #print(aaaaaaaaa)
    else:
        print("input an error number,please reinput")
        sys.exit(8)

