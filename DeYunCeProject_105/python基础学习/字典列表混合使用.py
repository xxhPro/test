"""
3张优惠券
    信息：名称 name，使用门槛money，发放限制 limit，type 满减券，还是折扣券

第一张：满300减50，300，1000，满减券
第二张：新人券，50，888，满减券
第三张：新品8折，100，999，折扣券
"""

coupon_1 = {'name': '满300减50', 'money': 300, 'limit': 1000, 'type': '满减券'}
coupon_2 = {'name': '新人券', 'money': 50, 'limit': 888, 'type': '满减券'}
coupon_3 = {'name': '新品8折', 'money': 100, 'limit': 999, 'type': '折扣券'}

coupon_list = [coupon_1, coupon_2, coupon_3]
print(coupon_list)


# 添加一张新券，中秋节8折券，200，limit 100，type 折扣券
coupon_list.append({'name': '中秋节8折券', 'money': 200, 'limit': 100, 'type': '折扣券'})
print(coupon_list)


# 修改第二张券的金额为 60

# coupon_2['money'] = 60


# 列表里面第二个元素

# coupon_list[1]  ->  coupon_2

# coupon_list[1]['money']  ->  coupon_2['money']

coupon_list[1]['money'] = 60
print(coupon_list)


# coupon_list[coupon_1,coupon_2,coupon_3,coupon_4]

# 删除每一张券的type

# 列表第0个元素    coupon_1  -> type    {'name': '满300减50', 'money': 300, 'limit': 1000, 'type': '满减券'}
# 列表第1个元素    coupon_2  -> type    {'name': '新人券', 'money': 50, 'limit': 888, 'type': '满减券'}
# 列表第2个元素    coupon_3  -> type    {'name': '新品8折', 'money': 100, 'limit': 999, 'type': '折扣券'}
# 列表第3个元素    coupon_4  -> type    {'name': '中秋节8折券', 'money': 200, 'limit': 100, 'type': '折扣券'}

# for coupon in coupon_list:
#     # 删除每张券的type
#
#     coupon.pop('type')
# print(coupon_list)


# 查找出面额大于100的券，符合条件的就输出

for coupon in coupon_list:
    if coupon["money"] > 100:

        print(coupon)
