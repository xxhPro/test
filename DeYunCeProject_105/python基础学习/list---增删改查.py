"""
高级数据类型-复合数据类型：

列表： list    利斯特
符号：[]，列表里面的值我们叫元素  [元素1, 元素2, 元素3, ...]

特点：
    1.有序
    2.可以按照下标取值，下标我们会叫索引
    3.可以存放不同数据类型的值，但是不建议，建议大家同类型的数据放在列表中
    4.可修改
    5.定义空列表  book_list = []
"""

# book_name_1 = '霸道总裁爱上我'
# book_name_2 = '十日终焉'
# book_name_3 = '活着'
# book_name_4 = 'QTP-自动化测试领航'
# book_name_5 = '骆驼祥子'

# book_list_1 = []
book_list = ['霸道总裁爱上我', '十日终焉', '活着', 'QTP-自动化测试领航', '骆驼祥子']

# print(type(book_list))


# 列表长度：len()
# 使用方法：len(列表名)
#
# 列表的取值：
#
# 1. 正向取值：通过下标，从 0 开始
# 例如：book_list[0] ～ book_list[最大长度-1]

# 2. 反向取值：通过下标，从 -1（最后一个值）开始
# 例如：book_list[-5] ～ book_list[-1]

# 3. 切片取值：book_list[起始值:结束值:步长]
# 起始值默认从 0 开始，切片会重新赋值给新的列表。左包含，右不包含。

# int_list = [1, 99, 88, 100, 678, 1093738]
#
# print(type(book_list))
#
# # 列表的长度 len(book_list)
# print(len(book_list))
#
#
# # 列表的取值
# book_1 = book_list[0]    # 取列表的第一个值
# print(book_1)
#
# print(book_list[2])
#
# print(book_list[-3])
#
# print(book_list[-1])

# 操作(重点)：

# 1.增加
# “append(元素值)”：默认放在列表最后
# “insert(下标, 元素值)”：根据下标，选择写入的位置
#
# 2.删
# “remove(元素值)”：删除指定的元素内容，如果列表中有重复元素，只删除第一个
# “pop()”：默认删除列表最后一个元素
# “pop(下标)”：删除指定下标对应的元素

# 3.改
# book_list[3] = 'QTP-自动化测试领航'

# 4.查：通过取值的方式，也叫取值（查询）：
# 1）通过下标取值：正向、反向取值
# 2）切片方式取值：`my_list[起始值:结束值:步长]`
# 3）`for` 循环遍历取值



# 元素的新增

# append()：默认把元素添加到列表的末尾
book_list.append("面纱")
print(book_list)

# insert(下标, 元素值)：根据指定下标，插入元素
book_list.insert(3, "何以笙箫默")
print(book_list)

# 元素的删除

# remove(元素值)：根据元素内容删除
# 如果列表中有重复元素，只删除第一个
book_list.remove('活着')
print(book_list)


# pop()：默认删除列表最后一个元素
book_list.pop()
print(book_list)


# pop(下标)：删除指定下标对应的元素
book_list.pop(3)
print(book_list)

book_list[3] = 'QTP-自动化测试领航'
print(book_list)

# 切片取值
# [:] 表示从头取到尾，相当于复制整个列表
new_book_list = book_list[:]
print(f'新列表:{new_book_list}')
print(f'原列表:{book_list}')

for book_name in book_list:
    print(book_name)
