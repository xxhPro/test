import os
import pytest


# pytest.main()  # 相当于在终端里面写了 pytest
# pytest.main(["-vs"])  # 相当于在终端里面写了 pytest -vs


# =========================================================
# 到目前为止  测试结果  只能在终端里面看  如果终端关闭  就不能看
# 为了以后也能看  需要把测试结果保存下来  生成一个报告
# 需要使用到 allure 插件   pip install allure-pytest


# pytest.main(["-vs","--alluredir","allure_data"])  # 相当于在终端里面写了pytest -vs --alluredir allure_data


# 生成测试结果数据
pytest.main(["-vs","--alluredir","allure_data","--clean-alluredir"])
# -vs  展示详细的信息 + 打印信息
#  "--alluredir","allure_data"  保存测试结果
#   --clean-alluredir  把之前的数据清空


# allure生成测试报告
os.system("allure generate ./allure_data -o allure_report --clean")

