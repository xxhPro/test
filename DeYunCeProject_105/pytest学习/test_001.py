"""
如果用例通过 展示一个点
如果用例失败 展示F

pytest -v  展示详细的信息
✅ pytest -vs  展示包括打印信息的详细信息


pytest -k   "关键词"  模糊匹配

    先找py文件，如果py文件匹配到关键词  里面的全部用例都会执行
    py文件找不到，继续找类，类里面的全部用例都会执行
    py文件找不到，继续匹配函数，函数匹配到直接执行

"""
import pytest


@pytest.mark.smoke_case
def test_login():
    print("正确的账号密码登录，预期结果正确")


@pytest.mark.smoke_case
def test_zhuce():
    print("注册成功")

