"""
1. 创建一个接口参数字典，包含code、msg、data三个字段，并使用打印取出code码。
   数据："code":200,"msg":"success","data":"你今天真棒！"
   如果 code码为200，打印输出“测试通过了”
2. 定义空字典，动态添加url、method、headers三个接口参数，最后遍历打印所有参数名和参数值。
3. 写一个无参函数，打印 “Python 自动化测试学习完成”
4. 写一个位置参数函数，接收用户名和密码，打印登录信息。
5. 写一个默认参数函数，默认打印 “测试环境登录”
6. 写一个带返回值的乘法函数，接收两个数字，返回和并做大小判断
7. 自己写一个重复的列表，然后通过集合去重，再转成列表
"""


# 1. 创建一个接口参数字典，包含code、msg、data三个字段，并使用打印取出code码
# 如果code码为200，打印输出“测试通过了”

api_data = {
    "code": 200,
    "msg": "success",
    "data": "你今天真棒！"
}

print(api_data["code"])

if api_data["code"] == 200:
    print("测试通过了")


# 2. 定义空字典，动态添加url、method、headers三个接口参数
# 最后遍历打印所有参数名和参数值

api_info = {}

api_info["url"] = "https://www.test.com/login"
api_info["method"] = "post"
api_info["headers"] = "application/json"

for k, v in api_info.items():
    print(f"{k} : {v}")


# 3. 写一个无参函数，打印“Python 自动化测试学习完成”

def study_python():
    print("Python 自动化测试学习完成")


study_python()


# 4. 写一个位置参数函数，接收用户名和密码，打印登录信息

def test_login(username, password):
    print(f"用户名：{username}")
    print(f"密码：{password}")


test_login("qingyue", "123456")


# 5. 写一个默认参数函数，默认打印“测试环境登录”

def login(env="测试环境登录"):
    print(env)


login()


# 6. 写一个带返回值的乘法函数
# 接收两个数字，返回乘积并做大小判断

def multiply(num1, num2):
    result = num1 * num2
    return result


number = multiply(10, 20)

print(number)

if number >= 100:
    print("结果大于等于100")
else:
    print("结果小于100")


# 7. 自己写一个重复的列表，然后通过集合去重，再转成列表

my_list = ["北京", "上海", "北京", "深圳", "上海", "杭州"]

my_set = set(my_list)
my_list = list(my_set)
print(my_list)
