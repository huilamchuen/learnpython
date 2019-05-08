"""
python 使用 lambda 来创建匿名函数。
1.lambda只是一个表达式，函数体比def简单很多。
2.ambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
3.lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
4.虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，
后者的目的是调用小函数时不占用栈内存从而增加运行效率。
"""
#lambda函数的语法只包含一个语句，如下：
#lambda [arg1 [,arg2,.....argn]]:expression
print("============普通python函数==========")
def func(x, y, z):
    return x + y + z
print(func(1, 2, 3))

print("============匿名python函数==========")
#冒号:之前的x,y,z表示它们是这个函数的参数
# 匿名函数不需要return来返回值，表达式本身结果就是返回值。
num = lambda x,y,z:  x+y+z
print(num(1,2,3))

print("============无参匿名python函数==========")
#无参匿名函数:
t = lambda : True #分号前无任何参数
print(t())
#带参数匿名函数
lambda x: x**2 #一个参数
lambda x,y,z:x+y+z #多个参数
lambda x,y=3: x*y #允许参数存在默认值

print("============带参匿名python函数==========")
#匿名函数调用
#直接赋值给一个变量,然后再像一般函数调用
t1 = lambda x: x**2 #一个参数
t2 = lambda x,y,z:x+y+z #多个参数
t3 = lambda x,y=3: x*y #允许参数存在默认值
print(t1(3))
print(t2(1,2,3))
print(t3(5))

print("============匿名python函数与列表连用==========")
L = [lambda x:x**2,lambda x:x**3,lambda x:x**4]
for f in L:
    #调用
     print (f(2))

print("============匿名python函数与字典连用==========")
dic = { 'A': lambda: 2*2,'B': lambda: 2*4,'C': lambda: 2*8}
print(dic['C']())