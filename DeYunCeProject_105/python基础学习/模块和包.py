"""
1. 模块(module)：就是一个.py文件
2. 包：多个模块放在一个目录下，目录就是包
    操作步骤：
        选中项目->新建 ->python 软件包
        区别：里面有一个 __init__.py
    包名不要以数字开头

3. 导入整个模块
使用：模块名.方法名()

import login
login.user_login()
login.user_login_out()

4. 导包的两种方式：
    第一种方式：
        导入整个模块
        使用：模块名.方法名()

    第二种方式：
        form 模块名 import 函数，变量
        from login import user_login

5. 重命名
    import software_package.product as p
    p.add_product()
    p.select_product()

"""