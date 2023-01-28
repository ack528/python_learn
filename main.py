# name = "山东工商学院"
# stock_price = 1000
# stock_code = 10086
# stock_price_daily_growth_factor = 1.2
# growth_days = 7
# print(f"公司{name}，股票代码{stock_code}，当前股价{stock_price}")#f为快速格式化
# print("每日增长系数是%.1f,经过%d增长后，股价达到了：%f"%(stock_price_daily_growth_factor,growth_days,(stock_price_daily_growth_factor**7)*stock_price))


# print("please input password:")
# password = input()
# print("the password is %s"%password)
# #or
# password = input("please input password:")
# print("the password is %s"%password)



# #input()默认输入的值都是字符串
# #其他类型需要类型转换
# password = input("please input password:")
# password = int(password)
# print("the password is %d"%password)



# #判断语句
# #python通过空格缩进判断所属
# age = 15
# if age >= 18:
#     print("成年了")
#     print("即将步入大学生活")
# elif age > 60:
#     print("老年人")
# else:
#     print("未成年")



# #随机数函数/while循环
# import random
# num = random.randint(1,100)
# flag = True
# count = 0;
# while flag:
#     count += 1
#     guess_num = input("请输入数字：")
#     guess_num = int(guess_num)
#
#     if guess_num == num:
#         print("猜对了")
#         flag = False
#     else:
#         if guess_num>num:
#             print("猜大了")
#         else:
#             print("猜小了")
# print(f"一共猜了{count}次")



# #print输出不换行
# print("1111",end='')
# print("2222",end='')



# #利用\t制表符对齐输出
# print("hello\tworld")
# print("hi\tworld")



# #输出九九乘法表
# x = 1
# y = 1
# while x <= 9:
#     y = 1
#     while y <= x:
#         print(f"{y}*{x}={x*y} ",end='')
#         y += 1
#     print()
#     x += 1



# #for循环 for临时变量in数据集
# #for循环无法定义循环条件，只能从被处理的数据集中，依次去除内容进行处理
# #所以，理论上讲，Python的for循环无法构建无限循环（被处理的数据集不可能无限大)
# name = "字符出"
# for x in name:
#     print(x)



# #range语句
# #range(n)获取一个从0开始，到num结束的数字序列(不含num本身)
# #range(num1,num2)获得一个从num1开始，到num2结束的数字序列（不含num2本身)
# #range(num1,num2,step)数字之间的步长，以step为准(step默认为1)
# for x in range(10):
#     print(x)



# #作用域
# for x in range(10):
#     print(x)
# print(x)#实际上是可以访问到的，但在编程规范上，是不允许、不建议这么做的



# #continue跳出本次循环，直接进行下次循环，break反同
# for x in range(1,5):
#     print("1")
#     continue
#     print("2")



# 练习题-发工资
# 某公司，账户余额有1W元，给20名员工发工资。
# 员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
# 领工资时，财务判断员工的绩效分（1-10)（随机生成)，如果低于5，不发工资，换下一位·如果工资发完了，结束发工资。
# import random
# total = 10000
# people = 1
# while people <= 20:
#     perf = random.randint(1,10)
#     if  total >0:
#         if perf > 5:
#             total = total -1000
#             print(f"员工{people}，绩效分{perf}，发工资1000元，余额还有{total}")
#         else:
#             print(f"员工{people}，绩效分{perf}，不发工资，下一位")
#     else:
#         print("工资发完了，下个月再来领吧")
#         break
#     people += 1



# #函数：是组织好的，可重复使用的，用来实现特定功能的代码段。
# name = "shandonggongshangxueyuan"
# length = len(name)
# print(length)



# #函数的定义
# # def 函数名（传入参数）：
# #     函数体
# #     return 返回值
# def print_hello():
#     print("hello")
# #函数调用
# print_hello()



# #函数传参练习
# #定义一个函数，名称任意，并接受一个参数传入（数字类型，表示体温)在函数内进行体温判断（正常范围:小于等于37.5度)
# def temp(x):
#     if x < 37.5:
#         print("体温正常")
#     else:
#         print("体温异常")
#
# y = input("请输入您的体温：")
# y = float(y)
# temp(y)



# #None用于声明无初始内容的变量
# name = None



#函数说明文档
# #格式如下
# def add(x,y):
#     """
#     add函数可以接受两个参数进行相加
#     :param x:参数一
#     :param y:参数二
#     :return:返回两参数的和
#     """
#     result = x + y
#     return result
#
# x = add(80,90)
# print(x)



# #在函数内修改全局变量，使用global 变量
# num = 100
# def test():
#     global num
#     num = 200
#
# test()
# print(num)



# 综合练习：atm
# def inquire():
#     global money
#     print(money)
#
# def deposit():
#     global money
#     deposit_money = input("请输入需要存的金额")
#     deposit_money = int(deposit_money)
#     money = money + deposit_money
#     print(money)
#
# def withdraw():
#     global money
#     withdraw_money = input("请输入需要取的金额")
#     withdraw_money = int(withdraw_money)
#     money = money - withdraw_money
#     print(money)
#
# key =0
# money = 5000000
# name = input("请输入姓名")
# while key != 4:
#     print("请按键输入选择需要的功能")
#     print("1.查询余额")
#     print("2.存款")
#     print("3.取款")
#     print("4.退出")
#     key = input()
#     key = int(key)
#     if key == 1:
#         inquire()
#     elif key == 2:
#         deposit()
#     elif key == 3:
#         withdraw()




# #数据容器：一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素每一个元素，可以是任意类型的数据，如字符串、数字、布尔等。
# #python有哪些数据容器：list(列表)、tuple(元组)、str(字符串)、set(集合)、dict(字典)
# #列表支持嵌套
# my_list = ["山东工商学院",666,True]
# my_list1 = [[1,2,3],[4,5,6]]
# print(type(my_list))
# #列表的下表索引
# print(my_list[0])
# #列表的反向索引：最后一个元素为-1
# print(my_list[-2])
# #嵌套列表去除元素
# print(my_list1[1][1])



# # 列表的方法：Python中，如果将函数定义为class（类)的成员，那么函数会称之为:方法
# # 方法和函数功能一样，有传入参数，有返回值，只是方法的使用格式不同:
# class student:
#     def add(self, x, y):
#         return x + y
#
# student = student()
# num = student.add(1, 2)
# print(num)



# #列表的下表索引功能
# #如果查找到元素不存在，程序会报错
# mylist = [111,222,333]
# search = mylist.index(222)
# print(search)
# #修改下表索引值
# mylist[0] = 444
# print(mylist)
# #插入元素:列表.insert(下标,元素)，在指定的下标位置，插人指定的元素
# mylist.insert(1,555)
# print(mylist)
# #追加元素
# mylist.append(666)
# print(mylist)
# #追加元素2：列表.extend(其它数据容器)，将其它数据容器的内容取出，依次追加到列表尾部
# mylist1=[888,999]
# mylist.extend(mylist1)
# print(mylist)
# #删除元素：
# # 1: del列表[下标]   2:列表.pop(下标)(取出元素，等同于删除，但是可以将取出的元素的以返回值得到)
# del mylist[0]
# print(mylist)
# # 2:列表.pop(下标)(取出元素，等同于删除，但是可以将取出的元素的以返回值得到)
# a = mylist.pop(0)
# print(a)
# print(mylist)
# #删除列表中匹配项
# mylist.remove(222)
# print(mylist)
# #清空列表
# mylist.clear()
# #统计列表元素数量
# mylist2 = [111,111,111,222]
# count = mylist2.count(111)
# print(count)
# #统计列表的全部元素数量
# count = len(mylist2)
# print(count)



# #列表的遍历--while循环
##取出元素
# def mylist_while_func():
#     flag = 0
#     mylist = [111,222,333]
#     while flag < len(mylist):
#         # 通过flag变量取出元素
#         print(mylist[flag])
#         flag += 1
# mylist_while_func()
# #列表的便利--for循环
# def mylist_for_func():
#     mylist = [111, 222, 333]
#     for element in mylist:
#         print(element)
#
# mylist_for_func()



# #元组：元组同列表一样，都是可以封装多个、木同类型的元素在内。但最大的不同点在于:
# #元组一旦定义完成﹐就不可修改
# t1 = (1,"hello",True)
# t2 = ()
# t3 = tuple()
# #***元组只有一个数据，这个数据后面要添加逗号
# t4 = (111,)
# #下标去内容
# t5 = ((1,2,3),(4,5,6))
# t6 = (1,2,2,2,2,1,1,3)
# print(t5[1][1])
# #index查找方法(返回值为下表)
# index = t6.index(2)
# print(index)
# #count方法
# print(t6.count(1))
# #元组不可以修改（增加或删除元素等)
# #but如果元组中嵌套了list，list可以修改
# t7 = (1,2,[4,5,6])
# t7[2][1] = 7
# print(t7)



# #字符串--不能进行内容修改
# mystr = "abcdefg"
# #下标索引
# print(mystr[1])
# #index
# index = mystr.index("c")
# print(index)
# #字符串替换：将字符串内的全部:字符串1，替换为字符串2
# #不是修改字符串本身，而是得到了一个新的字符串哦
# mystr1 = "111"
# mystr2 = mystr.replace("ab",mystr1)
# print(mystr2)
# #split方法：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
# #注意:字符串本身不变，而是得到了一个列表对象
# mystr3 = "1 2 3 4"
# mystr3_list = mystr3.split(" ")
# print(mystr3_list)
# #strip:字符串的规整操作(去前后空格)(不传参去空格，传参去指定字符)
# #注意传入的参数会被划分成一个个的字符，只要 前后  有符合的就会被去除，不考虑顺序
# mystr4 = "  111  "
# print(mystr4.strip())
# #count统计字符串中某字符串的出现次数
# #len统计字符串长度



# #序列是指:内容连续、有序，可使用下标索引的一类数据容器
# #列表、元组、字符串，均可以可以视为序列
# #序列的操作
# #切片：序列支持切片，即:列表、元组、字符串，均支持进行切片操作
# #切片:从一个序列中，取出一个子序列
# #表示从序列中，从指定位置开始，依次取出元素，到指定位置结束，得到一个新序列;
# #注意注意：中间是冒号，不是逗号
# #[:]表示从头到尾
# list = [0, 111, 222, 333, 444, 5555, 6666]
# result = list[1:4]
# print(result)
# #tuple
# tuple1 = (111,222,333,4,555,666)
# result = tuple1
# #反向切片
# # result = tuple1[::-1]
# # print(result)[:]
# # print(result)



# #集合{ , , , , }特点：不允许重复，顺序无法保证
# #空集合my_empty = set{}
# #
# #添加一个新元素
# my = {"好好哈",111,2222,3333}
# my.add(111)
# print(my)
# #删除一个元素
# my.remove(2222)
# print(my)
# #随机取出一个元素(注意是取出,取出后原集合该元素消失)
# result = my.pop()
# print(result)
# #清空集合
# my.clear()
# print(my)
# #取出2个集合的差集
# #语法:集合1.difference(集合2)，功能:取出集合1和集合2的差集
# #结果:得到一个新集合，集合1和集合2不变
# set1 = {1,22,333,444}
# set2 = {22,121,444,22}
# set3 = set1.difference(set2)
# print(set3)
# #消除2个集合的差集
# #语法:集合1.difference_update(集合2)
# #功能:对比集合1和集合2，在集合1内，删除和集合2相同的元素。
# set1 = {1,22,333,444}
# set2 = {121,444,22}
# set1.difference_update(set2)
# print(set1)
# print(set2)
# #2个集合合并
# #功能:将集合1和集合2组合成新集合
# #结果:得到新集合，集合1和集合2不变
# set3 = set1.union(set2)
# print(set3)
# #元素数量
# num  = len(set1)
# print(num)
# #集合的遍历(不能用while循环)
# set = {1,2,3,4,5}
# for num in set1:
#     print(num)



# #字典
# #定义：通过key找到相对应的value.所以字典的key是唯一的，不能重复
# #字典的定义，同样使用，不过存储的元素是一个个的:键值对，如下语法:
# #{key:value,key:value}
# #定义字典
# dic1 = {"stu1":99,"stu2":90,"stu3":22}
# #定于空字典
# dic2 = {}
# dic3 = dict()
# #字典同集合一样，不可以使用下标索引
# #但是字典可以通过Key值来取得对应的Value
# print(dic1["stu1"])
# #字典的嵌套
# dic4 = {"stu1":{"语文":90,"数学":77,"英语":33}}
# print(dic4["stu1"]["语文"])
# #新增元素
# #语法:字典[Key]=value，结果:字典被修改，新增了元素(前提key值不存在)
# dic2["stu1"] = 99
# print(dic2)
# #更新元素
# dic2["stu1"] = 66
# #删除元素
# #语法:字典ypop(Key),结果:获得指定Key的Value，同时字典被修改，指定Key的数据被删除
# score = dic2.pop("stu1")
# print(dic2)
# #清空元素
# dic1.clear()
# print(dic1)
# #获取全部的key
# keys = dic3.keys()
# print(keys)
# #遍历字典
# #方法一：通过获取全部的key来完成遍历
# for i in keys:
#     print(i)
#     print(dic2[i])
# #方法二：直接对字典进行for循环，每一次循环都是直接得到key
# for i in dic1:
#     print(dic1[i])
# #统计元素数量
# num = len(dic1)
# print(num)



#数据容器的通用操作
#len(),max(),min()
#转列表，转元组，转字符串，转集合//不能转字典
#通用排序：sorted(容器，[reverse=False])正向排序
#reverse=Ture  反向排序
#字符串大小比较：根据对应ascii码进行比较，按位比较//从头到尾一位位进行比较，其中一位大，后面就无需比较了。



# #函数进阶
# #函数的多返回值
# #如果函数有多个return，那么执行完其中一个return程序就会结束，不会在执行其他的return
# #多返回值函数的写法
# def muti():
#     return 1,2,3
# x, y, z= muti()
# print(x)
# print(y)
# print(z)
# #函数的传参方式
# #位置传参
# def user(name,age,gen):
#     print(f"{name}  {age}  {gen}")
# #关键字传参-可以不按位置传参
# user(age=10,name="xiaowang",gen="男")
# user("xiaohong",age=19,gen="女")
# #对应传参
# user("xiaowang",10,"男")
# #缺省传参(默认值)
# #//设置默认值需要统一在最后，如gen设置，或者age，gen设置
# def user1(name,age,gen = "男"):
#     print(f"{name}  {age}  {gen}")
# user1("xiaotian",17)
# user1("xiaotian",17,"女")
# #不定长参数
# #位置传递-args这个形参默认会标记为一个元组
# def user3(*args):
#     print(args)
# user3("xiaowang",10,23)
# #关键字传递-参数是“键=值”形式的形式,根据键-值组成字典
# def user4(**kwargs):
#     print(kwargs)
# user4(name="mingming",age=19,id=1232)
# #总结：位置不定长，*号，默认规范参数叫args
# #关键字不定长，**号，默认规范参数为kwargs



# #函数作为传入参数-传入的是代码的执行逻辑
# def func(com1):
#     result = com1(1,2)
#     print(result)
# def com(x,y):
#     return x + y
#
# func(com)
# #匿名函数-lambda定义匿名函数（无名称）
# #无名称的匿名函数只能临时使用一次
# #语法：1ambda传入参数:函数体(一行代码)
# #函数体，就是函数的执行逻辑，要注意:只能写一行，无法写多行代码
# #优点，简洁，缺点，只能用一次
# def func(com):
#     result = com(1,2)
#     print(result)
#
# func(lambda x,y:x+y)



# #python的文件操作
# #文件的编码-通过编码技术将内容翻译成0和1存入
# #文件的读取操作-打开-读写-关闭
# #打开函数open（name,mode,encoding）
# #mode指的是只读r 写入w 追加a
# f = open("C:/Users/31141/Desktop/project/python知识点/tset.txt","r",encoding="UTF-8")
# print(type(f))

# #read方法：文件对象.read(num)，num代表读取的字节，不填就全部读取
# print(f.read(3))

# #一个程序中多次调用read，下一个read会从上一个read结束处继续读取////
# print(f.read())

# #read.lines读取文件的全部行，封装到列表中//
# lines = f.readlines()
# print(lines)

# #read.line:一次读取一行，调用一次读取一行
# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)

# #for循环读取文件
# for line in f:
#     print(line)

# #文件的关闭-解除文件占用
# f.close()

# #with open() as f:-执行完语句自动关闭文件
# with open("C:/Users/31141/Desktop/project/python知识点/tset.txt","r",encoding="UTF-8") as f:
#     for line in f:
#         print(line)



# #写入操作
# f = open("C:/Users/31141/Desktop/project/python知识点/test1.txt","w",encoding="UTF-8")
# f.write("hello world")    #write会先将文件写入内存中
# f.flush()   #flush刷新，将内容写入硬盘中
# f.close()   #close自带flush功能


# #追加写入-有内容追加写入，没有内容创建文件后写入
# f = open("C:/Users/31141/Desktop/project/python知识点/tset1.txt","a",encoding="UTF-8")
# f.write("44444")
# f.close()


# #联系-账单
# f = open("C:/Users/31141/Desktop/project/python项目/原始账单.txt","r",encoding="UTF-8")
# f1 = open("C:/Users/31141/Desktop/project/python项目/新帐单.txt.bak","w",encoding="UTF-8")
# for line in f:
#     line1 = line.strip()      #取出开头结尾空格，换行符
#     words = line1.split(",")  #以空格为分隔
#     if words[4] == "测试":     #判断第五个元素
#         continue              #直接进入下一次循环
#     f1.write(line1)
#     f1.write("\n")            #补上回车
# f.close()
# f1.close()


# #了解异常-bug
# #异常的捕获方法：
# #异常的捕获方法：提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段。
# try:   #可能出现异常的代码
#     f = open("C:/Users/31141/Desktop/project/python项目/new.txt","r",encoding="UTF-8")
# except:   #如果出现异常，怎么补救（捕获所有异常）
#     f = open("C:/Users/31141/Desktop/project/python项目/new.txt", "w", encoding="UTF-8")
#
# #捕获指定的异常
# try:
#     print(name)
# except NameError as e:  #只捕获变量未定义的异常，其他异常还是会报错
#     print("变量未定义")
#
# #捕获多个异常
# try:
#     print(name)
#     1/0
# except (NameError,ZeroDivisionError) as e:  #只捕获变量未定义的异常，其他异常还是会报错
#     print("变量未定义或除零异常")
#
# #异常的else和finally
# try:
#     print("111")
# except:
#     print("异常")
# else:  #没有异常执行的代码
#     print("222")
# finally:  #有没有异常最终都要去执行，一般常用于文件的关闭
#     print("333")


# # #异常的传递
# # #看报错信息从下往上看
# # def func1():
# #     num = 1 / 0
# # def func2():
# #     func1()
# # def main():
# #     func2()
# # main()
#
# #捕获异常
# def func1():
#     num = 1 / 0
# def func2():
#     func1()
# def main():
#     try:
#         func2()
#     except Exception as e:
#         print(f"异常信息为:{e}")
#
# main()



# #python的模块（MOdule）：模块能定义函数，类和变量模块里也能包含可执行的代码.相当于一个工具包
# #语法[from模块名] import[模块│类│变量│函数│*][as 别名]
# import time #导入python内置的文件（按住ctrl同时鼠标点击，可以打开导入的文件）
# time.sleep(5)  #通过.符号表示层级
#
# #from部分导入
# from time import sleep  #只导入sleep这个方法
# sleep(5)
# #from全部导入
# from time import *
# sleep(5)
#
# #使用as给特定功能别名
# import time as t
# t.sleep(5)
#
# from  time import sleep as sl
# sl(5)



# #制作自定义模块
# #创建一个文件，然后导入
# import my_mudule1
# my_mudule1.add(4,6)

# #当导入两个模块中有同名函数时，调用函数时，执行的是后导入模块的函数
# from my_mudule2 import add
# from my_mudule2 import add
# add(9,6)

# #当导入模块时会默认执行模块的所有代码
# import my_mudule1


# #当python的模块过多时可以使用python的包进行管理，一个包里有多个模块
# #导入
# import my_package.module1
# my_package.module1.muti(4,6)
# from my_package.module2 import division
# division(24,3)


#安装第三方包-pip


# #数据可视化
# #json数据格式：JSON是一种轻量级的数据交互格式。可以按照JSON指定的格式去组织和封装数据
# #JSON本质上是一个带有特定格式的字符串,格式为列表，字典
# #功能：json就是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互
# #python转json  //注意时dumps不是dump
# import json
# list1 = [{"xiaowang":11},{"xiaohong":14},{"xiaoming":33}]
# json1 = json.dumps(list1,ensure_ascii=False)  #内容中有中文需要写后边的参数，没有中文，可以不写
# print(type(json1))
# print(json1)
# #将json字符串转换为python数据类型   //注意是loads不是load
# s1 = '[{"xiaowang":11},{"xiaohong":14},{"xiaoming":33}]'
# s2 = json.loads(s1)
# print(type(s2))
# print(s2)

# #数据可视化-基于pyechars的模块
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts
# line = Line()   #创建表格
# line.add_xaxis(["中国","美国","英国"])
# line.add_yaxis("GDP",[10,20,30])
# #全局配置方法
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True)
# )
#
# line.render()       #生成表格



# #对象
# #在程序中设计表格，称为设计类
# #在程序中打印生产的表格，为创建对象
# #在程序中填写表格，成为对象属性赋值
#
# #设计一个类
# class stu_list:
#     name = None
#     age = None
#     gender = None
#     score = None
# #创建一个对象
# stu1 = stu_list()
# #对象属性赋值
# stu1.name = "xiaohong"
# stu1.age = 18
# stu1.gender = "female"
# stu1.score = 90
# #获取对象信息
# print(stu1.name)



# #类的具体使用语法
# #class 类名称：
# #   类的属性，即定义在类中的变量（成员变量）
# #
# #   类的行为，即定义在类中的函数（类的方法）
#
# #定义类
# class stu_info:
#     name = None
#     age = None
#     def info(self):  #成员方法必须要有self，真正调用时忽略不传参
#         print(f"{self.name}的信息表格")#调用自身变量，必须加self
#     def hello(self,msg):
#         print(f"我是{self.name},{msg}")#外部传参不需要加self
# #创建对象
# stu1 = stu_info()
# #对象属性赋值
# stu1.name = "xiaoming"
# #获使用成员变量或者使用成员方法
# stu1.info()
# stu1.hello("你好啊")



# #现实世界事物都可以归纳为属性和行为
#
# #设计一个闹钟类
# class clock:
#     id = None
#     price = None
#
#     def ring(self):
#         import winsound
#         winsound.Beep(1000,3000)
# #构建闹钟对象
# clock1 = clock()
# #对象属性赋值
# clock1.id = "00001"
# clock1.price = 29
# #使用对象
# print(clock1.id)
# print(clock1.price)
# clock1.ring()



# #成员变量赋值-构造方法
# #构建类对象时直接以传参的方法进行赋值
# #__init__()方法-成为构造方法
# #在创建类对象（构造类）的时候会自动执行
# #在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
# class student:
#     name = None   #注意：上边三行可以不写，写了下边就是对成员变量赋值
#     age = None    #不写下边就是对成员变量声明并赋值
#     tel = None
#     def __init__(self,name,age,tel):    #根据定义init不调用就会执行，传入参数自动给到init
#         self.name = name
#         self.age = age
#         self.tel = tel
#
# stu1 = student("xiaoming",18,110)
#
# print(stu1.age)



# stu_list = []
#
# #练习学生信息录入系统
# class stu_info:
#     def __int__(self,name,age,tel):
#         self.name = name
#         self.age = age
#         self.tel = tel
#
# x = 1
# while x <= 10:
#     print(f"当前录入第{x}位学生信息，总共需要录入10位学生信息")
#     name = input("请输入学生姓名：")
#     age0 = input("请输入学生年龄：")
#     age = int(age0)
#     tel0 = input("请输入学生电话：")
#     tel = int(tel0)
#     stu = (name,age,tel)
#     print(f"学生{x}信息录入完成，信息为；【姓名{name},年龄{age}，电话{tel}】")
#     x += 1
# 未完成，提供方法，通过列表+字典存储



# #字符串代码-我们可以通过str_方法，控制类转换为字符串的行
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name}{self.age}"
# stu1 = Student("xiaohong",19)  #如果没有字符串方法，打印的是内存地址
# print(stu1)



# #__lt__用于两个类对象小于或大于符号比较方法
# #__le__用于两个类对象小于等于或者大于等于符号比较方法
# #__eq__用于两个类对象进行相等比较
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __lt__(self, other):
#         return self.age < other.age     #返回值Ture或者False
# stu1 = Student("xiaohong", 19)
# stu2 = Student("xiaoming", 22)
# print(stu1 < stu2)
# print(stu1 > stu2)



# #面向对象的封装特性
# #封装表示的是，将现实世界事物的属性和行为，封装为类的属性和行为
# #以两个下划线开头的变量和方法会变成私有无法对类对象使用，同时私有变量也无法获取值
# #私有成员无法被类对象使用，但是可以被其它的成员使用。
# class phone:
#     __current_voltage = 0.5        #当前手机的运行电压
#
#     def __keep_single_core(self):
#         print("使cpu以单核运行")
#
#     def call_by_5g(self):
#         if self.__current_voltage >= 1:
#             print("5g通话已开启")
#         else:
#             self.__current_voltage = 2
#             print("已经增压")
#             print(self.__current_voltage)
# applephone = phone()
#
# # applephone.__keep_single_core()   #私有成员方法无法使用
# #
# # print(__current_voltage)          #私有成员变量无法使用
#
# applephone.call_by_5g()



# #继承
# #单继承
# class phone2019:
#     Imei = None
#     producer = None
#
#     def call_by_4g(self):
#         print("4g通话")
# class phone2022(phone2019):     #把老的类的功能传给新的类
#     face_id = None
#
#     def call_by_5g(self):
#         print("5g通话")
#
# applephone = phone2022()
#
# applephone.Imei = 1011111
# applephone.producer = "apple"
# applephone.face_id = "xiaohong"
#
# #多继承
# class phone2024(phone2019,phone2022):
#
#     def flip(self):
#         print("屏幕已折叠")
#
# xiaomiphone = phone2024()
#
# xiaomiphone.Imei = 100000
# xiaomiphone.face_id = "xiaoliang"
# xiaomiphone.flip()
# #多继承也可以作为功能综合
# class phone2025(phone2019,phone2022,phone2024):
#     pass        #pass表示无内容，空的意思
#
# meizuphone = phone2025()
# meizuphone.Imei = 1999999



#复写：子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写。
#方法：在子类中//重新定义//同名的属性或方法即可.



# #调用父类的同名成员
# #调用父类成员变量  父类名.变量名
# #调用父类的成员方法   父类名.方法名
#
# class phone:
#     imei = None
#     producer = None
#     def call_by_5g(self):
#         print("使用5g通话")
#
# class phone1(phone):
#
#     def call_by_5g(self):
#         phone.call_by_5g(self)
#         print("使用单核通话")
#
# meizu = phone1()
# meizu.call_by_5g()



#类型注解：在代码中涉及数据交互的地方，提供数据类型的注解（显式的说明)。
#对变量进行注解
a1: float = 1.23
a2: bool = True
#对容器进行注解
list1 : list = [1,2,3]  #简易注解
list2 : list[int] = [1,2,3]  #详细注解
tuple1 : tuple[str,int,bool] = ("xiaoming",12,True)  #详细注解
dict1 : dict[str,int] ={"xiaohong":666}   #详细注解
#通过注释进行注解
a3 = 10  # type: int

from random import randint  #tips:alt+enter自动搜索并导入包
a4 = randint(1,10)   # type: int

#////写类型注解只在一眼看不出来返回值时才写类型注解，像上面写的能一眼看出来的，就不用写
#////同时类型注解只是注解作用，如果注解错了，也不会影响程序运行



# #函数（方法）的类型注解
# #def 函数名（形参名：类型，形参名：类型，形参名：注解）
# #对形参进行注解
# def add(x:int,y:int):
#     return x+y
# add(2,4)  #ctrl+p调出提示
# #对返回值进行注解 -> 返回值类型
# def func(data:list) -> list:
#     return data
#
#
#
# #使用Union类型进行联合注解
# #需要导入Union的包
# from typing import Union
# list3 : list[Union[str,int]] = ["wang",999,2323]
# dict2 : dict[str,Union[str,int]]={"xiaoliang":122,"xiaohong":"111"}
#
#
#
# #多态指的是:多种状态，即完成某个行为时，使用不同的对象会得到不同的状态。
# #以父类做声明，以子类实现

print("111")
print("222")
print("333")

