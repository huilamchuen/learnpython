#计算成绩
grade = int(input("请输入该同学的成绩"))
if grade >= 90:
    print("该同学成绩为：A")
elif grade >= 60 and grade <= 89:
    print("该同学成绩为：B")
else:
    print("该同学的成绩为：C")

# 整型  python中整形的运用，type()函数用户返回变量的类型
a = 5
print(a)
print(type(a))
#float 类型
b = 1.23
print(b)
print(type(b))
#Bool类型
c = True
d =False
print(c)
print(d)
print(type(c))
print(type(d))
#复数:complex
ac1 = 3 + 0.2j
print(ac1)
print(type(ac1))
ac2 = 4 -0.1j
print(ac2)
#导入cmath 模块
import cmath
#sqrt()是cmath 模块下的商数，用于计算平方根
ac3 = cmath.sqrt(-1)
print (ac3) #输出1j
#字符串  字符串的形式：使用‘’或者“”来创建字符串
name ='dingdongdong'
print(name)
#切片 获取切片，复数代表倒数第几个，从0开始
name ="dingdongdong"
print(name[1])
print(name[0:-2])#从第一个到倒数第二个，不包含倒数第二个
#列表（list）列表是由一系列特定元素顺序排列的元素组成的，它的元素可以是任何数据类型即数字、字符串、列表、元组、字典、布尔值等等，同时其元素也是可修改的。
list =[123,"dingdongdong"]
print(list)
#元组即为不可修改的列表。其于特性跟list相似。其使用圆括号而不是方括号来标识
list1 =(123,"dingdongdong")
print(list1)
#字典  --->dict类
#字典为一系列的键-值对，每个键值对用逗号隔开，每个键都与一个值相对应，可以通过使用键来访问对应的值。无序的。
#键的定义必须是不可变的，即可以是数字、字符串也可以是元组，还有布尔值等。
#而值的定义可以是任意数据类型。
#字典的定义
info ={
    1:"hello world",  #键为数字
    ("hello world"):1, #键为元组
    False:{
        "name":"James"
    },
    "age":22
}


