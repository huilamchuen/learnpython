'''
break
当在while或者for中使用break的时候break会跳出整个循环，也就是else里面的语句也不会执行，将跳出整个循环


for x in 'hello word!':
	if(x == 'o'):    #当遍历到o的时候跳出整个循环
		break
	print(x)
'''

'''
存在else的时候(if、while、for)当循环的条件为false时会执行else，
但再使用了break后，else中的内容也不会执行，因为它也属于一个循环体里的一部分
'''
count = 10
while(count > 0):
	if(count == 5):
		break
	print('    %d    '%count)
	count-=1
else:
	print('遍历完毕')


'''
continue
当在while或者for中使用continue的时候continue会跳过当前循环，然后再进入下一次循环，不会跳出整个循环，只是跳过符合continue的条件

break遍历到o会跳出整个循环，而continue不会跳出整个循环，而是跳过 'o' 以后继续遍历后面的字符
'''

for x in 'hello word':
	if(x == 'o'):
		continue
	print(x)





