#coding = utf-8

#计算1+2+3+4……+100的结果
a = 0
for i in range(1,101):
    a=a+i
    #a+=i
print(a)

#遍历字符串，纵向打印“不要说我不能”

a = "不要说我不能"
for i in a:
    print(i)

'''
函数语法 range是一个计数函数
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''

#for 重复一定次数的循环，称为计次循环（通常适用于枚举或遍历序列，以及迭代对象中的元素）
#while 一直重复，直到条件不满足时才结束的循环，条件循环，只要条件为真，循环会一直持续下云

for i in range(1,10,2):
    print(i,end='') #end=''不换行