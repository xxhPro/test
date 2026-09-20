"""
一、集合：set{}
    特点：
        1. 无序，无固定的下标
        2. 唯一，不可重复
        3. 创建一个空集合（特殊）：
            my_set = set()

        4. 操作：
            4.1 新增：
            add()  ->  my_set.add(值)
                例如：
                my_set = set()
                my_set.add("北京")

            作用：给集合中新增一个元素。

            4.2 删除：
            remove()  ->  my_set.remove(值)
            pop()  随机删除，了解即可

            4.3 取值：
            for 循环

        5. 使用（重点）：数据类型转换，去重
            去重：可以把列表的类型转成集合，去重之后，再转成列表。
            先使用 set() 把列表转换成集合，实现去重； 再使用 list() 把集合重新转换成列表。

        6. 运算：
            交集 (&)：取两个集合相同的部分
            并集 (|)：把两个集合合并，并去掉重复的部分
            差集 (-)：A集合 - B集合，得出来的结果是：【A有，B没有】
                    B集合 - A集合，得出来的结果是：【B有，A没有】


"""


# 列表转集合去重
# my_city = ['菏泽', '平顶山', '平顶山', '南阳', '成都', '上海', '阳泉', '运城', '上海']
#
# my_set = set(my_city)
# print(my_set)
#
# my_city = list(my_set)
# print(my_city)



# 元组转集合去重，输出的结果还是元组
my_tuple = ('菏泽', '平顶山', '平顶山', '南阳', '成都', '上海', '阳泉', '运城', '上海')

city_set = set(my_tuple)
my_tuple = tuple(city_set)
print(my_tuple)


my_set = set()

# 集合新增元素
my_set.add("小王子")
my_set.add("鲁滨逊漂流记")
my_set.add("老人与海")
my_set.add("钢铁是怎样炼成的")

print(my_set)


# 删除
# remove(值)：删除指定元素

# my_set.remove("小王子")
# print(my_set)


# 随机删除
# pop()：删除集合中的一个元素

# my_set.pop()
# print(my_set)


# 取值
# 集合没有下标，一般使用 for 循环遍历

for i in my_set:
    print(i)


# 定义两个集合
int_set_1 = {4, 6, 7, 8, 9, 188, 87, 56}
int_set_2 = {188, 56, 1, 2, 3, 7, 100, 999}

# 求交集：取两个集合中相同的元素
# 结果：{188, 56, 7}
print(int_set_1 & int_set_2)

# 求并集：把两个集合合并，并去掉重复元素
# 结果：{4, 6, 7, 8, 9, 188, 87, 56, 1, 2, 3, 100, 999}
print(int_set_1 | int_set_2)

# 求差集：取 int_set_1 中有，但 int_set_2 中没有的元素
# 结果：{4, 6, 8, 9, 87}
print(int_set_1 - int_set_2)

# 求反方向的差集：取 int_set_2 中有，但 int_set_1 中没有的元素
# print(int_set_2 - int_set_1)



