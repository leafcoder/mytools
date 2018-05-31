#!/usr/bin/python
#-*- coding: utf-8 -*-

import readline

threshold_point  = input('个税起征点：')
if not threshold_point:
    threshold_point = 3500 # 起征点：3500
while True:
    reserve = raw_input('是否缴纳公积金（Y/N），默认 Y：')
    reserve_percent = 0
    if not reserve or reserve.upper() == 'Y':
        reserve_percent  = 0.12  # 公积金
    pension_percent  = 0.08  # 养老
    medical_percent  = 0.02  # 医疗
    unemployment_fee = 10.65 # 失业
    base_fee = input('缴费基数： ')
    reserve = base_fee * reserve_percent
    pension = base_fee * pension_percent
    medical = base_fee * medical_percent
    wage = input('工资总额：')
    if not wage:
        continue
    income = float(wage) - threshold_point
    income = income - reserve - pension - medical - unemployment_fee
    if income <= 1500:
        tax_percent, remission = 0.03, 0
    elif income <= 4500:
        tax_percent, remission = 0.10, 105
    elif income <= 9000:
        tax_percent, remission = 0.20, 555
    elif income <= 35000:
        tax_percent, remission = 0.25, 1005
    elif income <= 55000:
        tax_percent, remission = 0.30, 2755
    elif income <= 80000:
        tax_percent, remission = 0.35, 5505
    else:
        tax_percent, remission = 0.45, 13505
    total_tax = income * tax_percent - remission
    if total_tax < 0:
        total_tax = 0
    income = income - total_tax + threshold_point
    print
    print '公 积 金：', reserve
    print '养老保险：', pension
    print '医疗保险：', medical
    print '失业保险：', unemployment_fee
    print '生育保险：', 0
    print '工伤保险：', 0
    print '纳税总额：', total_tax
    print '实际收入：', income
    print
