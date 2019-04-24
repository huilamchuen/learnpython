#作业一
#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
#【input()、if elif else、 print】
score = int(input("请输入你的分数："))
if score >= 90:
    print("你的成绩是A")
elif 60<=score<=89:
    print("你的成绩是B")
else:
    print("你的成绩是C")

#二、6个类型
#作业二
# 2、举例说明3个基本数据类型的使用
#1.int
age = 18
print(age)
print(type(age))

#2.float
money = 34.50
print(money)
print(type(money))

#3.str
name1 = "小红"
name2 = "小花"
print(name1)
#字符串重复
print(name2*50)
#字符串拼接
print(name1+name2)
print(type(name1+name2))
#字符串下标访问
name3 = "helloworld"
print(name3)
print(name3[1])
print(name3[-2])
#字符串切片（截取）
print(name3[0:5]) #hello

#4.BOOL
a=True
b=False
print(a)
print(b)
print(type(a))
print(type(b))

#5.list（列表）是一种有序的集合，可以随时添加、修改、删除其中的元素。
#1.创建列表
list = []
list1 = [20,37,39,27,42]
list2 = [20,30,49,"好日子",True,89.12]
print(list1)
print(list2)
#2.访问列表中的元素,元素下标有两个，正向和负向
print(list1[0])
print(list2[-1])
#3.修改列表中的元素
list1[0] = 50
print(list1)
#4.追加列表中的元素
list3 = list1 + list2
print(list3)
#用append()函数，可以在列表末尾添加元素
print(list2)
list2.append("好好学习，天天向上")
print(list2)
#5.删除元素
del list2[5]
print(list2)

'''6.Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
'''
#创建元组
tup = ()
tup1 = ('Google', 'baidu', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
print(tup1)
print(type(tup1))
#访问元组
print(tup1[1])
print(tup1[-1])
# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)
#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tup3
#print(tup3)
#元组截取
print(tup2[0:2]) #(1, 2)

#字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
#访问
print ("dict['Name']: ", dict['Name'])
#修改字典
dict['Age'] = 8 # 更新
dict['School'] = "中关村小学" # 添加
print(dict)