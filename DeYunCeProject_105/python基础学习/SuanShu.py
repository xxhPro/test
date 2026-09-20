# 测试执行场景数据

total_case = 230      # 本轮总测试用例数量
pass_case = 195       # 通过用例
fail_case = 28        # 失败用例
tester_num = 3        # 测试人员数量


# 1. 加法：计算已执行的用例数
executed_case = pass_case + fail_case
print("已执行用例数：", executed_case)


# 2. 减法：计算未通过的用例数量
not_pass_case = total_case - pass_case
print("未通过用例数量：", not_pass_case)


# 3. 乘法：执行2轮回归，计算总执行用例数
total_execute_case = total_case * 2
print("执行2轮后的总用例数：", total_execute_case)


# 4. 普通除法：计算测试通过率
pass_rate = pass_case / total_case * 100
print("测试通过率：", pass_rate,"%")


# 5. 整除：平均分给3个测试人员
average_case = total_case // tester_num
print("每人基础分到的用例数：", average_case)


# 6. 取余：计算分配后剩余的用例
remain_case = total_case % tester_num
print("剩余用例数：", remain_case)


# 7. 幂运算：计算5的6次方
result = 5 ** 6
print("5的6次方：", result)