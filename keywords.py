#coding = utf-8
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))#len获取对象长度

'''
del 删除变量
from引用模块时会用到
golbal为全局变量，但当单个函数中出现同一变量名时，在单个函数中为局部变量
with被用来处理异常try
assert 断言，声明其布尔值必须为真的判定，如果发生异常就说明表达示为假
pass是空语句，为了保证程序结构的完整性，不做任何事情，一般用作 占位语句
yield的意思是生产，返回了一个生成器对象，每个生成器只能使用一次
break语句用来终止循环，用在while和for循环中
break是跳出整个循环，continue是跳出当前循环
=============================================
'''
'''用来定义的关键字
def : 定义一个函数或方法；
class: 定义一个类对象；
lambda：定义一个匿名函数；
   布尔关键字
False:代表真；
True：代表假；
   控制流关键字
if...elif...else...:条件判断；
for...in...:对可迭代对象循环遍历
for...in...else...:遍历正常完成则执行else后的代码；
continue:终止本次循环，继续下一次循环；
break：跳出循环；
while：循环结构；
   逻辑判断关键字
and:表示与
or：表示或；
not：表示非；
in：判断元素是否在容器内；
not in：判断元素是否不再容器内；
is:比较两个变量的内存地址；
   异常
try:
代码1
except:
代码2
else：
代码3
finally：
代码4...
# 代码1发生异常就执行代码2，正常就执行代码3，无论正常与否都要执行代码4.
raise：主动触发异常

    命令空间
global:将模块空间变量引入到局部空间修改；
nonlocal:将本局部空间的外层空间变量引入到本层局部空间修改，用来嵌套函数内；
    其他
None:代表空，是python解释器的一个内置的关键字变量；本质是一个object()
from ... import ...:从模块导入对象
import ... :导入模块
import ... as ...:导入模块指定别名
with:触发上下文管理器；
assert：断言，True则通过，False则触发异常；
pass：表示跳过，用来防止报错；
return：函数返回值；
yield：生成器关键字；
del：从上下文堆栈中删除某个对象
'''