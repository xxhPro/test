"""
字典：dict{}

    1. 特点：无序、可变的数据结构，使用键值对的方式进行存储。
    {key: value}其中：
        key 就是字典的键，value 就是 key 对应的值。

    2. 定义：
    创建一个空字典：
        my_dict = {}
    创建一个字典：
        my_dict = {key1: value1, key2: value2, ...}

    3. 取值：
    字典名[key]  ->  my_dict['name']，没有对应的key，程序会报错：KeyError: 'job'
    字典名.get(key)  ->  my_info.get('name')
    如果 字典名.get(key),key值不存在，返回 None，程序不会报错，可以设置默认值
    例如：print(my_info.get('job','没有这个键'))

    4. 操作：
    增/改：key，有则改，无则增
        4.1 增加：字典名[key] = 值，key在字典中不存在
        4.2 修改：字典名[key] = 值，key在字典中存在
        4.3 删除：pop()  ->  字典名.pop(key)  ->  my_info.pop("job")

    5. 三种遍历方式：

        5.1 取出所有的键值    字典名.keys()
        for k in my_info.keys():
            print(k)

        5.2 取出所有的 value 值    字典名.values()
        for v in my_info.values():
            print(v)

        5.3 取出所有的键值（key:value）对    字典名.items()
        for k, v in my_info.items():
            print(k, v)

    *** json 与 字典 的区别 ***

1. json 是一种文本格式，本质上是一个字符串（是一种数据传递的格式规范。比如，前后端的交互），字典是 python 里特有的一个数据类型
2. json 里面的 key 必须是双引号，字典里面的 key 单引号、双引号都可以
3. json 里面的 bool 类型是小写：true / false，字典里面：True / False
4. json 里面的空值 null，字典里面的空值是 None



"""

# 定义一个空字典
my_dict = {}
print(type(my_dict))


# 创建一个字典
my_info = {
    'name': 'qingyue',
    'age': 18,
    'hobby': '徒步',
    'gender': '女'
}

print(my_info)

# # 取出字典不存在的键 会报错 KeyError: 'job'
# print(my_info['job'])


# get方法取值  ->  字典名.get(key)
print(my_info.get('name'))
# 使用get方法取一个不存在的键    None 在python中是空值    null
print(my_info.get('job'))
# print(my_info.get('job','没有这个键'))

# 字典增加值
my_info['job'] = '老师'
print(my_info)

# 字典修改
my_info['job'] = '小丑'
print(my_info)

# 字典删除
my_info.pop("job")
print(my_info)


# # 遍历所有的key
# for k in my_info.keys():
#     print(k)

# 遍历所有values
for v in my_info.values():
    print(v)

# 遍历所有的键值对
for k, v in my_info.items():
    print(f'{k} : {v}')
