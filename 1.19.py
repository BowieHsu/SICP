#encoding:utf-8
__author__ = 'bowiehsu'
'''
对数步数求斐波那契数列
'''
def fib(n):
    return fib_iter(1,0,0,1,n)
def fib_iter(a,b,p,q,count):
    if count == 0:return b
    else:
        if count %2 == 0:
            return fib_iter(a,b,p**2+q**2,2*p*q+q**2,count/2)
        else:return fib_iter(b*q+a*q+a*p,b*p+a*q,p,q,count-1)

print fib(6)