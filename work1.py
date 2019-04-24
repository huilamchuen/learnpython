#python 关键字

#true、false
import keyword
print(keyword.kwlist)
print("----------------------------")
#酒精含量 if 语句
Alcohol = int(input("请输入酒精含量"))
if Alcohol < 20:
    print("不构成酒驾")
elif 20 <= Alcohol < 80:
    print("饮酒驾车")
else :
    print("醉酒驾车")

#for 循环
sum = 0
number = 1
for n in range(1,101):
    sum+=n
print ("1到%d的总和为：%d" %(n,sum))

#纵向打印 遍历字符串 for in 的方式
x="不要说我不能"
for str in x:
    print (str)
#纵向打印 遍历字符串 rang() 的方式
x="再来试一种方式"
for index in range(len(x)):
    print(x)
    print("----------------")
    print(x[index])
#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        d = j * i
        print('%d*%d=%-2d'%(j,i,d),end = ' ' )
    print()
#

