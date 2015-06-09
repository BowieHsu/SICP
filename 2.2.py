#encoding:utf-8
__author__ = 'bowiehsu'
'''
元组的闭包性质
'''
a,b,c = (1,2,3)
print a,b,c
a1,b1 = ((1,2),(3))
print a1,b1

A = [1,2,3,4]
B = (1,2,3,4)
C = list(B)
print A,C