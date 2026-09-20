"""
人：
    1. 特征：
    两条胳膊
    两条腿
    姓名
    性别
    身高
    体重
    年龄

    2. 行为：
    讲话
    睡觉
    吃饭


奶茶：
    1. 固定的配方
    大杯/中杯/小杯
    无糖、少少糖、正常糖、8分糖
    常温、加冰

    2. 行为：
    加奶

    3. 制作：
    摇匀


手机：
    1. 特征：
    品牌
    颜色
    型号
    内存


    2. 行为：
    打电话
    发短信
    刷短视频
    拍照

一、类：
    静态特征
    动态行为

    *** 面向对象三大特点 ***：
    封装、继承、多态

    定义类：
    class 类名(首字母要大写，行业规范):
        pass
    实例化对象  ->  根据类（模板） 创建一个具体的对象

    1. 写法：
    对象名 = 类名()  ->  通过类的模板，创建一个具体的对象

    2. 初始化方法：
    def __init__(self,name,age,gender):

    3. 执行的时机：
    类创建对象的时候，会默认执行 __init__(self) 方法

    4. 初始化的属性： 比如 name，age，gender，可以通过传参的方式给到这个初始化方法
    这样在创建对象的时候，就把属性的值给到对象

    5. self：代表对象自己
    举例：person_1 = Person("qingyue",18,'女')，person_1 是被创建的对象（实例化）的对象，那么 self 就代表 person_1

    6. 实例方法：
    def speak(self):
        print(f"{self.name}在讲话")

    7. 使用方法：
    类创建出来的对象【实例化对象】.实例方法()  ->  person_1.speak()

    8. 继承：
    语法格式：class 类名(父类名)
    class Student(Person):
        pass

    子类可以直接调用父类的实例属性和实例方法

    

"""


# 定义了一个类 Person，相当于是一个模版
# class Person:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
#     def speak(self):
#         print(f"{self.name}在讲话")
#
#
# # 创建一个类的对象，需要是一个具体的人
# person_1 = Person("qingyue", 18, '女') # 创造一个具体的人 person_1 -> 实例化一个对象
# # print(person_1)
# person_1.speak()


# 在写一个实例化方法 吃饭，打印 self.name 在吃饭
# 创建一个对象，调用吃饭的方法
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 实例方法：讲话
    def speak(self):
        print(f"{self.name}在讲话")

    # 在写一个实例化方法 吃饭，打印 self.name 在吃饭
    def eat(self):
        print(f"{self.name}在吃饭")


# 创建一个对象，调用吃饭的方法
# person_1 = Person("qingyue", 18, "女")
# person_1.eat()


# 创建了一个 Student 类，继承 Person 类
# 类需要继承的时候才要加（）
class Student(Person):
    def study(self):
        print(f"{self.name}要学习")



stu_1 = Student("qingyue", 18, "女")
stu_1.eat()
stu_1.study()




# 定义个奶茶的类 BubbleTea
class BubbleTea:
    pass


# 定义一个手机的类
class MobilePhone:
    pass





