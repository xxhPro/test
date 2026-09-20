"""
类型转换

str -> 整型 int()
str -> 浮点型 float()
int -> str()
float -> str()
"""


# 输入商品名称，价格，数量，计算商品总价
# goods_name = input("请输入商品名称：")
# goods_price = float(input("请输入商品价格："))
# goods_num = int(input("请输入商品数量："))
# total_price = goods_price * goods_num    # float(goods_price)
#
# print(f"总价为{total_price}")


# 整型转成字符串
number = 3
str_number = str(number)
print(type(str_number))

# 浮点型转成字符串
fl = 3.98768
str_fl = str(fl)
print(type(str_fl))
