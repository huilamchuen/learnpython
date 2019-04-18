

while True:
    scroe = input("请输入得分：")
    if scroe.isnumeric() == True:
        scroe = float(scroe)
        x = scroe
        break
    else:
        print("输入失败,必须输入为数字，请重新输入")
print(x)

if x > 89:
    print("恭喜你；A")
elif (x > 60 and x < 90):
     print("B")
else:
    print("C")







