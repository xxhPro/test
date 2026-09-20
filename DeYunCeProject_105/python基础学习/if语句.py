"""
if 条件：
    执行的代码

如果你有 100
    买房
    捐出去

如果我有 1000000：
    打印 我想周游世界
"""

# I = float(input("请输入你的存款："))
#
# if I >= 1000000:
#     print("我想周游世界")


# 双分支语句
# me = int(input("我的存款有:"))
#
# if me >= 1000000:
#     print("我想周游世界")
# else:
#     print("我想周游中国")


# if 条件(bool):
#     执行代码        注意点：缩进，tab
# else:
#     条件不满足执行代码    注意点：缩进，tab

# bool 类型
# 单值比较：>=、<=、>、<、!=、==
#
# 条件1 and 条件2
#
# 条件1 or 条件2

# height = int(input("输入你的身高:"))
# money = int(input("输入你的存款:"))
#
# if height >= 178 and money >= 10000000:
#     print("你是高富帅")
# else:
#     print("你是普通人")



# 从控制台接收 身高 和 存款
#
# 如果 身高大于等于 178cm，存款达到 10000000
# 打印：你是高富帅
#
# 如果 身高大于等于 178cm，存款达到 200000
# 打印：你只是个子高
#
# 如果 身高小于 178，存款 >= 10000000
# 打印：你只是有钱
#
# 否则：
# 打印：你是普通人


# 多分支语句
# height = int(input("请输入你的身高："))
# money = int(input("请输入你的存款："))
#
# if height >= 178 and money >= 10000000:
#     print("你是高富帅")
#
# elif height >= 178 and money >= 200000:
#     print("你只是个子高")
#
# elif height < 178 and money >= 10000000:
#     print("你只是有钱")
#
# else:
#     print("你是普通人")


# 练习：
# 从控制台输入你的成绩 score
#
# 如果 成绩 >= 90，打印【优秀】
# 如果 成绩 80~89 之间，打印【良好】
# 如果 成绩 70~79 之间，打印【中等】
# 如果 成绩 60~69 之间，打印【合格】
# 否则 打印【准备迎接混合双打】

# score = int(input("请输入你的成绩："))
#
# if score >= 90:
#     print("优秀")
#
# elif score >= 80:
#     print("良好")
#
# elif score >= 70:
#     print("中等")
#
# elif score >= 60:
#     print("合格")
#
# else:
#     print("准备迎接混合双打")


# 系统随机生成一个数
import random
random_number = random.randint(1, 100)
print(random_number)
