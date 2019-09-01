#!/usr/bin/env python3
# coding:utf-8
'''
随机银行卡
'''
import copy
import json
import math
import random

import requests

# 维萨卡（VISACARD）
VISA_PREFIX_LIST = [
    "4539", "4556", "4916", "4532", "4929", "40240071", "4485", "4716", "4"
]
# 万事达卡（MasterCard）
MASTERCARD_PREFIX_LIST = ["51", "52", "53", "54", "55"]
# 美国运通卡（AmericanExpressCard）
AMEX_PREFIX_LIST = ["34", "37"]
# 发现卡(Discover Card)
DISCOVER_PREFIX_LIST = ["6011"]
# 大莱卡（DinersCard）
DINERS_PREFIX_LIST = ["300", "301", "302", "303", "36", "38"]
# enRoute（credit card issued by Air Canada until 1992）
ENROUTE_PREFIX_LIST = ["2014", "2149"]
# JCB卡（JAPANCREDITBUREAUCARD）
JCB_PREFIX_LIST = ["35"]
# Voyager Credit Card
VOYAGER_PREFIX_LIST = ["8699"]
# 中国银联
China_UnionPay_PREFIX_LIST = ["62"]
# 常用
CUP_PREFIX_LIST = {
    '622220': '中国工商银行',
    '622258': '中国交通银行',
    '622707': '中国建设银行',
    '622580': '中国招商银行',
    '622150': '中国邮政储蓄银行',
    '622273': '中国银行',
    '623058': '平安银行'
}
BANK_CODE_LIST = {
    'CCB': '中国建设银行',
    'ABC': '中国农业银行',
    'ICBC': '中国工商银行',
    'CDB': '国家开发银行',
    'BCCB': '北京市商业银行',
    'HSBC': '汇丰银行',
    'PBC': '中国人民银行',
    'BOC': '中国银行',
    'CMBC': '中国民生银行',
    'CMB': '招商银行',
    'CIB': '兴业银行',
    'BCM': '交通银行',
    'CEB': '中国光大银行',
    'GDB': '广东发展银行',
    'SPABANK': '平安银行'
}
CARD_TYPE_LIST = {'DC': "储蓄卡", 'CC': "信用卡", 'SCC': "准贷记卡", 'PC': "预付费卡"}


def completed_number(ccnumber, length):
    # generate digits
    while len(ccnumber) < (length - 1):
        digit = str(random.randint(0, 9))
        ccnumber = ccnumber + digit
    # Calculate sum
    sum = 0
    pos = 0
    reversed_ccnumber = []
    reversed_ccnumber.extend(ccnumber)
    reversed_ccnumber.reverse()
    while pos < length - 1:
        # 卡号从右往左看，偶数位数乘以2
        odd = int(reversed_ccnumber[pos]) * 2
        # 如果乘以2后的数为两位数(值大于9)则减去9
        if odd > 9:
            odd -= 9
        # 然后将所有的位数进行累加
        sum += odd
        if pos != (length - 2):
            sum += int(reversed_ccnumber[pos + 1])
        # 偶数位从0开始，加2循环
        pos += 2
    # Calculate check digit
    # 最后一位当做是校验位，用来补齐到能够整除10
    # TODO
    # t = 10 - sum % 10
    # ccnumber += str(0 if t == 10 else t)
    # math.floor 向下取整
    checkdigit = int(((math.floor(sum / 10) + 1) * 10 - sum) % 10)
    ccnumber = str(ccnumber) + str(checkdigit)
    # TODO end
    return ccnumber


def get_bank_number(prefixList=None, length=None):
    if prefixList is None:
        prefixList = list(CUP_PREFIX_LIST.keys())
    if length is None:
        length = 16
    ccnumber = copy.copy(random.choice(prefixList))
    ccnumber = '622707'
    bank_number = completed_number(ccnumber, length)
    return bank_number


def is_bank_number(bank_number):
    try:
        url = 'https://ccdcapi.alipay.com/validateAndCacheCardInfo.json?\
        _input_charset=utf-8&cardNo=%s&cardBinCheck=true' % bank_number
        r = requests.get(url)
        data = r.text
        data = json.loads(data)
        # print(data)
        validated = data['validated']
        cardType = None
        bank = None
        if validated is True:
            cardType = CARD_TYPE_LIST[data['cardType']]
            bank = BANK_CODE_LIST[data['bank']]
            print(cardType, bank)
        return validated, cardType, bank
    except Exception as e:
        if isinstance(bank_number, int):
            bank_number = str(bank_number)
        mod10Count = 0
        reversed_ccnumber = list(reversed(bank_number))

        for i in range(0, len(bank_number) - 1):
            augend = reversed_ccnumber[i]
            if ((i + 1) % 2) == 0:
                productString = str(augend * 2)
                augend = 0
                for j in range(0, len(productString)):
                    augend += int(productString[j])
            mod10Count += int(augend)
        digits = [int(x) for x in reversed(str(bank_number))]
        check_sum = sum(digits[::2]) + sum(
            (dig // 10 + dig % 10) for dig in [2 * el for el in digits[1::2]])
        print(check_sum, mod10Count)
        return (mod10Count % 10) == 0


if __name__ == "__main__":
    bank_number = '6217000010104124329'
    bank_number = get_bank_number()
    print(bank_number)
    print(is_bank_number(bank_number))
