#!/usr/bin/python
# -*- coding: UTF-8 -*-

str=input("请输入分数：")

try :
    score = int( str )
    if score>= 90 :
        print("您的分数为; A")
    elif 60 <= score <= 89 :
        print( "您的分数为:  B" )
    else :
        print( "您的分数为: C" )

except :
    print("对不起，您输入的不是数字，请重新输入！")