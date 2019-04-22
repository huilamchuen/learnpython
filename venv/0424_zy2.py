'''
 监督检验检疫局发布的《车辆驾驶人员血液、呼气酒精含量阈值与检验》中
 车辆驾驶人员每100毫升血液中的酒精含量小于20mg不构成饮酒驾驶行为:
 酒精含量大于或等于20mg、小于80mg为饮酒驾车:
 酒精含量大于或等于80mg为醉酒驾车
 现编写段 Python代码判断是否酒后驾车
'''
def jiujia(jiujing):
    if jiujing >=80:
        print("醉酒驾车")
    elif score>=20:
        print("饮酒驾车")
    else:
        print("非酒驾")
while 1:
    jiujing= int(input('请输入每100ml的酒精含量：'))
    jiujia(jiujing)
