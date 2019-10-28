"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: Tsubame
Date: 2019-10-28
"""
from math import sqrt

num = int(input("请输入一个正整数："))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime == True and num != 1:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)
