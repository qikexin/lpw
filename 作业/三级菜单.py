#author:lpw
#date:
import pickle
# def dump_pickle():
#     user={1:"q",2:"w",3:"ads"}
#     with open("test.pickle","wb") as f:
#         pickle.dump(user,f)
#         print("success")
# def load_pickle():
#     with open("test.pickle","rb") as f:
#         user=pickle.load(f)
#         print(user)
#
# # dump_pickle()
# load_pickle()

jiadian={
    "家电":{
        "冰箱":{
            "海尔":"$450",
            "创维":"$500"
        },
        "洗衣机":{
            "全自动":"$470",
            "半自动":"$300"
        },
        "电视":{
            "创维":"$890",
            "乐视":"$930"
        }
    }
}
yifu={
    "衣服":{
        "上衣":{
            "衬衣":"￥86",
            "毛衣":"￥50",
            "羽绒服":"￥500"
        },
        "下衣":{
            "牛仔裤":{
                "颜色":"蓝色",
                "尺寸":"32",
                "价格":"￥150"
            },
            "休闲裤":{
                "颜色":"浅蓝色",
                "尺寸":"32",
                "价格":"￥200"
            }
        },
        "鞋":{
            "运动鞋":{
                "滑板鞋":"$30",
                "足球鞋":"$48"
            },
            "皮鞋":{
                "皮革":"$57",
                "牛皮":"$70"
            }
        }
    }
}
shouji={
    "手机":{
            "联通":{
                "华为":"$300",
                "小米":"$60"
            },
            "电信":{
                "华为":"$290",
                "小米":"$60"
            },
            "移动":{
                "华为":"$310",
                "小米":"$70"
            }
        }
    }
che={
    "车":{
        "自行车":{
            "moble":"￥399",
            "ofs":"￥99"
        },
        "电动车":{
            "爱马仕":"$130",
            "小鸟":"$120"
        },
        "汽车":{
            "宝马":"$13000",
            "奔驰":"$9999"
        }
    }
}

menu={1:jiadian,2:yifu,3:shouji,4:che}
def first_menu(num):
    if num == 1:
        for k1 in  jiadian.keys():
            key1=k1
        for k2 in yifu.keys():
            key2=k2
        for k3 in shouji.keys():
            key3=k3
        for k4 in che.keys():
            key4=k4
        # print(jiadian.keys(),yifu.keys(),shouji.keys(),che.keys())
        # a=jiadian.keys()
        # b=yifu.keys()
        # c=shouji.keys()
        # d=che.keys()
        print("1: "+key1+" 2： "+key2+" 3: "+key3+" 4: "+key4)
    return key1,key2,key3,key4
def second_menu(key):
    Second_Menu=[]
    i=1
    if key == "家电":
        for key1_1 in jiadian["家电"].keys():
            # print(key1_1)
            Second_Menu.append(key1_1)
        print("输出二级菜单:(家电类)")
        for j in range(1,len(Second_Menu)+1):
            print("%d:%s" % (j,Second_Menu[j-1]))
        # print(Second_Menu)
        return  Second_Menu
    elif key == "衣服":
        for key2_2 in yifu["衣服"].keys():
            Second_Menu.append(key2_2)
        print("输出二级菜单:(衣服类)")
        for j in range(1,len(Second_Menu)+1):
            print("%d:%s" % (j,Second_Menu[j-1]))
        # print(Second_Menu)
        return  Second_Menu
    elif key == "手机":
        for key3_3 in shouji["手机"].keys():
            Second_Menu.append(key3_3)
        print("输出二级菜单:(手机类)")
        for j in range(1,len(Second_Menu)+1):
            print("%d:%s" % (j,Second_Menu[j-1]))
        # print(Second_Menu)
        return  Second_Menu
    elif key == "车":
        for key4_4 in che["车"].keys():
            Second_Menu.append(key4_4)
        print("输出二级菜单:(车类)")
        for j in range(1,len(Second_Menu)+1):
            print("%d:%s" % (j,Second_Menu[j-1]))
        # print(Second_Menu)
        return  Second_Menu
def third_menu(key):
    if key == "洗衣机":
        for i in jiadian["家电"][key].items():
            print(i[0]+" : "+i[1])
    if key == "电视":
        for i in jiadian["家电"][key].items():
            print(i[0]+" : "+i[1])
    if key == "冰箱":
        for i in jiadian["家电"][key].items():
            print(i[0]+" : "+i[1])
    if key == "上衣":
        for i in yifu["衣服"][key].items():
            print(i[0]+" : "+i[1])
    if key == "下衣":
        for i in yifu["衣服"][key].items():
            print(i[0]+" : "+i[1])
    if key == "鞋":
        for i in yifu["衣服"][key].items():
            print(i[0]+" : "+i[1])
    if key == "联通":
        for i in shouji["手机"][key].items():
            print(i[0]+" : "+i[1])
    if key == "电信":
        for i in shouji["手机"][key].items():
            print(i[0]+" : "+i[1])
    if key == "移动":
        for i in shouji["手机"][key].items():
            print(i[0]+" : "+i[1])
    if key == "自行车":
        for i in che["车"][key].items():
            print(i[0]+" : "+i[1])
    if key == "电动车":
        for i in che["车"][key].items():
            print(i[0]+" : "+i[1])
    if key == "汽车":
        for i in che["车"][key].items():
            print(i[0]+" : "+i[1])
# third_menu("洗衣机")
# third_menu("电视")
# third_menu("冰箱")
# third_menu("上衣")
# third_menu("下衣")
# third_menu("鞋")
# third_menu("联通")
# third_menu("电信")
# third_menu("移动")
# third_menu("自行车")
# third_menu("电动车")
# third_menu("汽车")

if __name__ == '__main__':
    print("输出一级菜单：")
    # first_menu(1)
    TAG=1
    tag = 1
    key1,key2,key3,key4=first_menu(1)
    print("查看二级菜单请输入菜单编号,退出请输入q或者Q")
    while TAG != 0:
        num = input("请输入菜单编号")
        while tag != 0:
            if num == "家电":
                if tag == 1:
                    second = second_menu("家电")
                num2=input("输入数字查看三级菜单，“r”返回上一级菜单,“q”退出程序")
                if num2 == "r":
                    first_menu(1)
                    tag =1
                    break
                elif num2 == "q":
                    TAG=0
                    break
                else:
                    # print("输出三级菜单")
                    # print(second)
                    # num3=input("输入数字查看三级菜单，“r”返回上一级菜单,“q”退出程序")
                    num3 = num2
                    print("输出三级菜单")
                    if num3 == "洗衣机":
                        third_menu("洗衣机")
                        # print(jiadian["家电"]["洗衣机"].items())
                    elif num3 == "电视":
                        third_menu("电视")
                        # print(jiadian["家电"]["电视"].items())
                    elif num3 == "冰箱":
                        third_menu("冰箱")
                        # print(jiadian["家电"]["冰箱"].items())
                    elif num3 == "r":
                        first_menu(1)
                        tag = 1
                        continue
                    elif num3 == "q":
                        exit(0)
                    else:
                        print("输入错误，程序退出！")
                        exit(1)
                tag=2
                continue
            elif num == "衣服":
                if tag == 1:
                    second_menu("衣服")
                num2=input("输入数字查看三级级菜单，“r”返回上一级菜单,“q”退出程序")
                if num2 == "r":
                    first_menu(1)
                    tag = 1
                    break
                elif num2 == "q":
                    TAG = 0
                    break
                else:
                    # print("输出三级菜单")
                    num3 = num2
                    print("输出三级菜单")
                    if num3 == "上衣":
                        third_menu("上衣")
                    elif num3 == "下衣":
                        third_menu("下衣")
                    elif num3 == "鞋":
                        third_menu("鞋")
                    elif num3 == "r":
                        first_menu(1)
                        tag = 1
                        continue
                    elif num3 == "q":
                        exit(0)
                    else:
                        print("输入错误，程序退出！")
                        exit(1)
                tag=2
                continue
            elif num == "手机":
                if tag == 1:
                    second_menu("手机")
                num2=input("输入数字查看二级菜单，“r”返回上一级菜单,“q”退出程序")
                if num2 == "r":
                    first_menu(1)
                    tag = 1
                    break
                elif num2 == "q":
                    TAG = 0
                    break
                else:
                    # print("输出三级菜单")
                    num3 = num2
                    print("输出三级菜单")
                    if num3 == "联通":
                        third_menu("联通")
                    elif num3 == "电信":
                        third_menu("电信")
                    elif num3 == "移动":
                        third_menu("移动")
                    elif num3 == "r":
                        first_menu(1)
                        tag = 1
                        continue
                    elif num3 == "q":
                        exit(0)
                    else:
                        print("输入错误，程序退出！")
                        exit(1)
                tag=2
                continue
            elif num == "车":
                if tag == 1:
                    second_menu("车")
                num2=input("输入数字查看二级菜单，“r”返回上一级菜单,“q”退出程序")
                if num2 == "r":
                    first_menu(1)
                    tag = 1
                    break
                elif num2 == "q":
                    TAG = 0
                    break
                else:
                    # print("输出三级菜单")
                    num3 = num2
                    print("输出三级菜单")
                    if num3 == "自行车":
                        third_menu("自行车")
                    elif num3 == "电动车":
                        third_menu("电动车")
                    elif num3 == "汽车":
                        third_menu("汽车")
                    elif num3 == "r":
                        first_menu(1)
                        tag = 1
                        continue
                    elif num3 == "q":
                        exit(0)
                    else:
                        print("输入错误，程序退出！")
                        exit(1)
                tag=2
                continue

            else:
                print("输入错误，程序退出")
                exit(2)




