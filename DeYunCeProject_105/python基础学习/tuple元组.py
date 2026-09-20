"""
元组：`tuple`
符号：`()`
特点：
* 1. 有序
* 2. 不可修改：重点关注
* 3. 特殊：如果元组里面只有一个元素，要加逗号，例如 my_tuple = (1,)

# 元组长度：len()
# 使用方法：len(元组名)

# 元组的取值：
# 1. 正向取值
#    通过下标，从 0 开始
#    例如：book_tuple[0] ~ book_tuple[最大长度 - 1]

# 2. 反向取值
#    通过下标，从 -1（最后一个值）开始
#    例如：book_tuple[-5] ~ book_tuple[-1]

# 3. 切片
#    book_tuple[起始值:结束值:步长]
#    起始值默认从 0 开始
#    左包含，右不包含

# book_tuple[1:3]
# 只能取到下标为 1、2 的值，不会取到下标为 3 的值

# book_tuple[:]
# 默认获取全部元素

# 操作：
# 只有查：通过取值的方式

# 类型转换

"""


# 定义元组

my_tuple = ()
print(type(my_tuple))

my_tuple_1 = ("string",)
print(type(my_tuple_1))

# 定义元组
env_tuple = ("test", "stage", "gray", "pro")

# 元组取值
print(env_tuple[2])


# 类型转换

# 将元组转换成列表
env_list = list(env_tuple)

# 修改列表中下标为 1 的元素
env_list[1] = "uat"

print(env_list)

# 再将列表转换成元组
env_tuple = tuple(env_list)

print(env_tuple)

for env_name in env_tuple:
    print(env_name)
