#coding = utf-8

#break是终止本次循环，
# 比如有很多个for循环，在其中一个for循环里写了一个break，满足条件，只会终止这个for里面的循环，
# 程序会跳到上一层for循环继续往下走

for i in 'Python':
   if i == 'o':
      break
   print("打印当前字母",i)

#continue 语句跳出本次循环，而break跳出整个循环。
#continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
#continue语句用在while和for循环中。

for i in 'Python':
   if i == 'h':
      continue
   print("打印当前字母",i)

#pass 是空语句，是为了保持程序结构的完整性。
#pass 不做任何事情，一般用做占位语句

for i in 'Python':
   if i == 'h':
      pass
      print("passsssss")
   print("打印当前字母",i)