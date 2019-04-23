# 1、利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# 【input()、if elif else、 print】

score = float (input("请输入学生成绩：") )
print ("您输入的学生成绩为： ",score)
if score >= 90:
    print("成绩等级为：A")
elif score >= 60:
    print("成绩等级为：B")
else :
    print("成绩等级为：C")