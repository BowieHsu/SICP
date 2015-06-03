#encoding:utf-8
__author__ = 'bowiehsu'
'''
只用对数的步数计算幂指数
'''
def fast_expt(x,n):
    if n == 0:return 1
    elif n%2 == 0: return fast_expt(x,n/2)**2
    else : return x*fast_expt(x,n-1)

def a_fast_expt(a,x,n):
    return a * fast_expt(x,n)
'''
对数步骤求乘法
'''
def plus(a,b):
    if b == 0:return 0
    elif b%2 == 0: return plus(a,b/2)*2
    else:return a+plus(a,b-1)

print plus(2,7)
