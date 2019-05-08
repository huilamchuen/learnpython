"""
一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里定义（赋值）的。
变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：
全局变量和局部变量
"""
print("===================11111==================")
#定义了同名的全局变量和局部变量，函数内部优先访问局部变量
num = 1 #全局变量
def my_fun(x,y,z):
    num = x+y+z  #局部变量
    print("1111函数内的num值是:", num)
my_fun(2,3,5)
print("1111函数外的num值是:", num)


print("===================22222=================")
#只定义了全局变量，函数内部可以访问全局变量，但不能修改全局变量的值；函数外不能访问局部变量
num = 1 #全局变量
def my_fun(x,y,z):
    print("2222函数内的num值是:", num)
    return num
my_fun(1,2,5)
print("2222函数外的num值是:", num)


print("=================33333==================")
#在函数内部修改全局变量的值，要用global关键字
num = 1 #全局变量
def my_fun(x,y,z):
    global num
    num = 8
    print("3333函数内的num值是:", num)
    return num
my_fun(1,2,5)
print("3333函数外的num值是:", num)