#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''

Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表 ）有序、Dictionary（字典）无序、Set（集合）无序。

'''


# 数字类型： Python3 支持 int、float、bool、complex（复数）
a, b, c, d = 20, 5.5, True, 4+3j
print(a,b,c,d)

#
# 字符串类型：Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
# str = 'Runoob'
# print( str )  # 输出字符串
# print( str[0:-1] )  # 输出第一个到倒数第二个的所有字符
# print( str[0] )  # 输出字符串第一个字符
# print( str[2:5] )  # 输出从第三个开始到第五个的字符
# print( str[2:] )  # 输出从第三个开始的后的所有字符
# print( str * 2 )  # 输出字符串两次
# print( str + "TEST" )  # 连接字符串


#列表：列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

# list = ['abcd', 786, 2.23, 'runoob', 70.2]
# tinylist = [123, 'runoob']
# print( list )  # 输出完整列表
# print( list[0] )  # 输出列表第一个元素
# print( list[1:3] )  # 从第二个开始输出到第三个元素
# print( list[2:] )  # 输出从第三个元素开始的所有元素
# print( tinylist * 2 )  # 输出两次列表
# print( list + tinylist )  # 连接列表

#元祖:元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

# tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
# tinytuple = (123, 'runoob')
#
# print( tuple )  # 输出完整元组
# print( tuple[0] )  # 输出元组的第一个元素
# print( tuple[1:3] )  # 输出从第二个元素开始到第三个元素
# print( tuple[2:] )  # 输出从第三个元素开始的所有元素
# print( tinytuple * 2 )  # 输出两次元组
# print( tuple + tinytuple )  # 连接元组


#集合：集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员，可以使用大括号 { } 或者 set() 函数创建集合
#
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
#
# print( student )  # 输出集合，重复的元素被自动去掉
#
# # 成员测试
# if 'Rose' in student:
#     print( 'Rose 在集合中' )
# else:
#     print( 'Rose 不在集合中' )
#
# # set可以进行集合运算
# a = set( 'abracadabra' )
# b = set( 'alacazam' )
#
# print( a )
#
# print( a - b )  # a 和 b 的差集
#
# print( a | b )  # a 和 b 的并集
#
# print( a & b )  # a 和 b 的交集
#
# print( a ^ b )  # a 和 b 中不同时存在的元素

#字典：字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
#
# tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
#
# print( dict['one'] )  # 输出键为 'one' 的值
# print( dict[2] )  # 输出键为 2 的值
# print( tinydict )  # 输出完整的字典
# print( tinydict.keys() )  # 输出所有键
# print( tinydict.values() )  # 输出所有值