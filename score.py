#coding = utf-8

score = float(input("请输入分数："))
if score >= 90:
    print("分数为:%s" %("A"))
elif score >= 60:
    print("分数为: %s" %("B"))
else:
    print("分数为: C")