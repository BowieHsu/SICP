#encoding:utf-8
__author__ = 'bowiehsu'
'''寻找一个数的最大因子
'''
def smallest_divisor(n):
    return find_divisor(n,2)

def find_divisor(n,divisor):
    if divisor**2 > n:return n
    if n%divisor == 0 :return divisor
    else:return find_divisor(n,divisor+1)

print smallest_divisor(1105)