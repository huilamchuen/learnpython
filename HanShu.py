#函数的定义：
"""函数是可以实现一些特定功能的小方法或是小程序。
在Python中有很多内建函数，当然随着学习的深入，你也可以学会创建对自己有用的函数。
简单的理解下函数的概念，就是你编写了一些语句，为了方便使用这些语句，把这些语句组合在一起，给它起一个名字。
使用的时候只要调用这个名字，就可以实现语句组的功能了"""
#什么时候用函数
"""1、一段代码需要重复使用的时候用函数会减少代码量
   2、在开发过程中,某部分代码被使用多次，我们就需要把这部分代码封装成一个小模块，这个模块就是函数。
   3、函数用于简化程序结构，增加阅读行，实现代码复用
   4、函数分为声明函数和调用函数"""
def print_hello():#声明函数
    print("你好世界")#函数内容

print_hello()#调用函数
print("------------------------")

#二、函数的创建（内置函数）
def hello(name):
    return 'hello,' + name +'!'
print('dingdongdong')
print("------------------------")

#函数的调用
def calcu(x, y):#x,y叫形参
    print("x的值是%d"%x)
    print("y的值是%d"%y)
    z = x + y
    print(z)

calcu(1,2)#1,2叫实参
print("------------------------")

# 定义函数
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return

# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
print("------------------------")
#传不可变的参数
def ChangeInt(a):
    a = 10
b = 2
ChangeInt(b)
print(b)
print("")
#传可变的参数——可变参数就是允许在调用参数的时候传入多个（≥0个）参数（类似于列表、字典）
def calc(l):
    sum = 0
    for n in l:
        sum += n
    return sum

calc([1,2,3])
print("------------------------")
#默认参数——在调用函数的时候使用一些包含默认值的参数
def power(x, n=2):
    s = 1
    while(n > 0):
        n -=1
        s *=n
    return s

power(3)
power(2, 3)

#【关键字参数】
#关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
#使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

#实例一
def printme(str):
    #"打印任何传入的字符串"
    print ("str 的值为：",str);
    return
# 调用printme函数
printme(str="My string");

#实例二 对位置的不限定更明显
def printinfo(name, age):
    #"打印任何传入的字符串"

    print("Name: ", name);
    print("Age ", age);
    return
# 调用printinfo函数
printinfo(age=50, name="miki");



#return语法——return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
#return实例1
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total

# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)

#return实例2
def printinfo(name, age=35):
    #"打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)

# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")

#全局变量和局部变量
#定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
#局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中

total = 0  # 这是一个全局变量

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total

# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)








