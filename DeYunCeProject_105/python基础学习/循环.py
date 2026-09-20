# 循环：
#重复的执行一段代码

# 方式一：
# for i in 序列:
#     循环体(代码)

# import random
# random_number = random.randint(1, 100)

# for i in [1, 2, 3]:
#     guess_number = int(input("数字"))
#
#     if random_number == guess_number:
#         print("你真棒")
#
#     elif random_number > guess_number:
#         print("猜小了")
#
#     else:
#         print("猜大了")

# for i in range(10):
#     guess_number = int(input("请输入你猜的数字："))
#
#     if random_number == guess_number:
#         print("我们真是心有灵犀!!!")
#         continue
#         # print("不要着急，还有大的惊喜哦!!!")
#
#     elif random_number > guess_number:
#         print("你猜小了!")
#
#     else:
#         print("你猜大了")


# 方式二：
# while 条件（bool）:
#     循环体(代码)

# 解释：只要条件满足，就一直循环，直到条件不满足，跳出循环。
# 不确定次数的情况下，要使用 while 循环（重点关注）。

# i = 1
#
# while i < 6:
#     print(i)
#     i = i + 1


# 逻辑：

# 第一次循环：i = 1，i < 6，打印 i = 1，i = 2
# 第二次循环：i = 2，2 < 6，打印 i = 2，i = 3
# 第三次循环：i = 3，3 < 6，打印 i = 3，i = 4
# 第四次循环：i = 4，4 < 6，打印 i = 4，i = i + 1 = 5
# 第五次循环：i = 5，5 < 6，打印 i = 5，i = 6
# 第六次循环：i = 6，6 < 6，不会在循环内部走了

# 练习：
#     输出 20 以内的奇数

for i in range(1, 21):
    if i % 2 != 0:
        print(i)

