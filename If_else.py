
#if嵌套举例
str=input("请输入酒精含量：")
try :
   alcohol = int(str)
   if alcohol >= 20:
      if 20 <= alcohol <=80:
        print("该人员为饮酒驾车")
      else:
        print("该人员为醉酒驾车")

   else:
        print("该人员不构成酒驾行为")
except:
    print("对不起，您输入的不是数字，请重新输入！")