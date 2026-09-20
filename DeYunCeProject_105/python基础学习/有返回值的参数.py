"""
    返回值函数
        def 函数名(形参1,形参2,....):
            函数体
            return 函数结果值
    举例：
        def add(num1,num2):
            num = num1 + num2

            return num
"""


# 写个加法的函数
def add(num1,num2):
    num = num1 + num2
    return num

# number = add(80,70)

# print(number)

if add(80,70) >= 180:
    print("哇，你真棒")

else:
    print("你还需要努力")

# 判断 这个 加起来的值大于等于180, print("哇，你真棒")
# 判断 这个 加起来的值小于180, print("你还需要努力")



