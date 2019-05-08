# 关键字参数-实例说明
"""
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

以下实例在函数 printme() 调用时使用参数名：
"""
print("=====================关键字参数===================")
def my_fun(name,age):
    print("%s is a good girl,she is %d years old"%(name,age))
#调用my_fun函数
my_fun(age=20,name="小花")

print("=====================默认参数===================")
"""
调用函数时，默认参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：
"""
def my_fun(name,age=15):
    print("%s is a good girl,she is %d years old"%(name,age))
my_fun(age=21,name="小华")
#不传入age的值
my_fun(name="小华")

print("=====================可变参数===================")
"""
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，
和上述2种参数不同，声明时不会命名。基本语法如下：
加了星号（*）的变量名会存放所有未命名的变量参数。
"""
def my_fun1(name,*args):
    print(args,type(args))
my_fun1("xiaohua",1,2,3,4,5)

def my_fun1(name,**kwargs):
    print(kwargs, type(kwargs))
my_fun1("xiaohua",x=1,y=2,z=3)
