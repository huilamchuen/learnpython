def grade(score):
    if score >=90:
        print("A")
    elif score>=60:
        print("B")
    else:
        print("C")
while 1:
    score = int(input('输入分数：'))
    grade(score)