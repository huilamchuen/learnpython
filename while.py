#coding = utf-8

i=1
while i<=3:    #while -表达式且，为真i=1 i<=3 为真，输入结果，一直循环
    print("我可以")
    i+=1       #加限定条件，i=i+1  4时为假，终断循环
'''
实例：
模拟输入密码6次错误，无法进入系统
'''

password = 0
i = 1
while i < 7:
    num = int(input("请输一位数字密码"))
 #   num = int(num)
    if num == password:
        print("密码正确，进入系统")
        i=7                              #加个条件，为假时，终断循环，循环结束，
    else:
        print("密码错误，已经输错",i,"次")
    i=i+1
if i== 7:
    print("密码输错6次，请与管理员联系！")