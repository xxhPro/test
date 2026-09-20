"""

input()、print()、int()、float()、str()、type()、list()、tuple()、len()

"""

# list.sort()  → 修改原列表，返回 None ,所以 print(list.sort()) 返回的是 null
# sorted(list) → 不修改原列表，返回一个新的排序列表

my_list = [9, 5, 89, 164, 1, 7467, 765]

my_list.sort()
print(my_list)


new_my_list = sorted(my_list)
print(my_list)
print(new_my_list)


# 列表从大到小

my_list = [9, 5, 89, 164, 1, 7467, 765]
my_list.sort(reverse=True)
print(my_list)

# 字符串的拼接

str_1 = "welcome to "
str_2 = "deyunce"
print(str_1 + str_2)

# * 在字符串中的使用

str_3 = " = "
print(str_3 * 20)



# 作业5：列出元组与列表有哪些区别？

# 1. 元组不可修改，列表可修改，共同点：都是有序的
# 2. 元组是 tuple()，列表是 list[]
# 3. 元组的访问速度会更快一些，列表的访问速度会慢一点
