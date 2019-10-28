"""
输入两个正整数计算它们的最大公约数和最小公倍数

Version: 0.1
Author: Tsubame
Date: 2019-10-28
"""
x = int(input("请输入x："))
y = int(input("请输入y："))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor ==0:
        print('%d和%d最大公约数是：%d' % (x, y, factor))
        print('%d和%d最小公倍数是：%d' % (x, y, x * y // factor))
        break
