"""
生成斐波那契数列的前二十位

Author: Tsubame
Date: 2019-11-6
"""
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=" ")