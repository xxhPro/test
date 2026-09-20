"""
写文件
1、创建/打开文件
2、写入内容
3、保存文件并关闭


两种方式：
    第一种：
        #'文件' -> 要写入的文件名，没有会自动创建，'w' -> 写模式，encoding = 'utf-8' 是编码格式，中文不会乱码
        file = open('文件','w',encoding = 'utf-8')
        file.write(内容)
        file.close

    第二种：
        # 固定写法 with open(...) as file
        with open('文件','w',encoding = 'utf-8') as file:
            file.write(内容)


读文件：
1、打开文件
2、读取内容
3、关闭


"""



# 第一种写文件
file = open("deyunce.txt",'w',encoding = "utf-8")
file.write("hello world!!! \n")
file.write("欢迎你们来到德云测")  # 不写 utf-8 的话这里会报错
file.close()

# 第二种写文件，不需要手写去关闭
with open("101.txt",'w',encoding="utf-8") as file:
    file.write("Hello world!!! \n")
    file.write("欢迎你们来到德云测")


# 追加 模式改成 a ->append  追加
with open("101.txt",'a',encoding="utf-8") as file:
    file.write("我希望你们都可以找到高薪的工作 \n")
    file.write("希望你们未来可期")
print("文件已写入")


# 读文件 -> 读取全部内容
with open("101.txt",'r',encoding="utf-8") as file:
    content = file.read()
print(content)


# 读文件 -> 文件内容读取到列表中
with open("101.txt",'r',encoding="utf-8") as file:
    content = file.readlines()
print(content)


# 读文件 -> 只读取一行
with open("101.txt",'r',encoding="utf-8") as file:
    content = file.readline()
print(content)

