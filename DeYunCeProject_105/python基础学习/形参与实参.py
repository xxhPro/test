"""
有参函数：
    位置参数
        def 函数名(形参1,形参2,形参3,....):
            函数体
        特点：
            位置必须一一对应
            数量必须一一对应，不能多也不能少
        形参：形式参数，主要是为了占位

    调用：
        函数名(实参1,实参2,实参3,....)
    实参：实际要传入的参数值

    关键字参数：
        def 函数名(形参1,形参2,形参3,....):
            函数体

        调用：
        函数名(形参2 = 实参2,形参1 = 实参1,...)


    默认值参数：
        def 函数名(形参 = 默认值):
            函数体

        调用：
            函数名()
            函数名(实参)


"""


# 定义函数

# def test_login(username,password):
#     print("先打开网址")
#     print(f"输入用户名:{username}")
#     print(f"输入密码{password}")
#     print("输入验证码")
#     print("点击登录")
#     print("跳转到对应的页面")
#
#
# # 调用函数
# # test_login("qingyue","123456")
#
# test_login(password = '123456',username = "qingyue" )


def learn_python(job = "软件测试工程师"):
    print(f'我来德云测学习的目标是成为一名{job}')

# learn_python()

learn_python("测试开发工程师")


# 位置参数一定要放在默认参数前面，下面的写法是错误的
# def test_login(password = "123456",username):
#     print("先打开网址")
#     print(f"输入用户名:{username}")
#     print(f"输入密码{password}")
#     print("输入验证码")
#     print("点击登录")
#     print("跳转到对应的页面")
# 
# test_login("qingyue")

