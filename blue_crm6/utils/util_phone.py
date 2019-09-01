#!/usr/bin/env python3
# coding:utf-8
'''
获取随机手机号方法
'''
import random
import time
'''
MDN号码的结构如下：CC + MAC + H0 H1 H2 H3 + ABCD：
【CC】：国家码，中国使用86。
【MAC】：移动接入码，本网采用网号方案，为133。
【H0H1H2H3】：HLR识别码，由运营商统一分配。
【ABCD】：移动用户号，由各HLR自行分配。
'''
# 号段列表
macid_list = [
    '133', '149', '153', '173', '177', '180', '181', '189', '199', '130',
    '131', '132', '145', '155', '156', '166', '171', '175', '176', '185',
    '186', '166', '134', '135', '136', '137', '138', '139', '147', '150',
    '151', '152', '157', '158', '159', '172', '178', '182', '183', '184',
    '187', '188', '198'
]


# 获取随机手机号
# return int
def get_phone(macid=None):
    if macid is None:
        macid = random.choice(macid_list)
    elif macid not in macid_list:
        return
    # 地区4位，取本机月日
    H0H1H2H3 = time.strftime("%m").zfill(2) + time.strftime("%d").zfill(2)
    # 随机4位数，zfill方法使高位补0
    ABCD = str(random.randint(0, 9999)).zfill(4)
    phone = str(macid) + H0H1H2H3 + ABCD
    # print(phone)
    return int(phone)


if __name__ == "__main__":
    p = get_phone
    print(p)
