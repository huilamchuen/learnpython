"""
range() 函数可创建一个整数列表，一般用在 for 循环中。
函数语法
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
"""
s = range(0,10,2)
print(list(s))#[0, 2, 4, 6, 8]
#步长默认为1
s1 = range(1,10)
print(list(s1)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#开始默认是0
s2 = range(10) #range（10）等价于range（0， 10）
print(list(s2))