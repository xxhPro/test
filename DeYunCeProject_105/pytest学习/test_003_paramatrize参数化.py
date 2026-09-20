import pytest

@pytest.mark.parametrize("account, pwd, exp", [
    ("10086", "a123456", "登录成功"),
    ("13012312300", "a123456", "登录失败")
])
def test_deng_lu(account, pwd, exp):
    """
    :param account: 账号
    :param pwd: 密码
    :param exp: 预期
    :return: 返回值
    """
    print(f"使用的账号密码是：{account}/{pwd}, 预期结果是：{exp}")


