# 任务二if嵌套if相关
# 实战场景1：国家质量监督检验检疫局发布的《车辆驾驶人员血液、呼气酒精含量阈值与检验》中车辆驾驶人员每100毫升血液中的酒精
# 含量小于20mg不构成饮酒驾驶行为:酒精含量大于或等于20mg、小于80mg为饮酒驾车:酒精含量大于或等于80mg为醉酒驾车。
# 现编写段 Python代码判断是否酒后驾车
#

jjhl = int (input("请输入测量酒精含量(mg)："))
if jjhl < 20 :
    print("您不构成酒后驾车，请小心")
else:
    if jjhl < 80:
        print("饮酒驾车，快死了吧")
    else:
        print("您醉酒还驾车，死翘翘了！！！")

# has_ticket = input()
# knife_length = int(input())
# if has_ticket:
#     print("车票检查通过，准备开始安检")
#     if knife_length <20:
#         print("刀的长度有 %d 厘米，不超过20厘米，允许上车" % knife_length)
#     else:
#         print("刀的长度有 %d 厘米，超过20厘米，不允许上车" % knife_length)
# else:
#     print("没有车票，不允许进站")
