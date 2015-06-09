#encoding:utf-8
__author__ = 'bowiehsu'
'''
定义一个过程cubic
'''
def cubic(a,b,c):
    return lambda x:x**3+a*x**2+b*x+c
    #return newton_method()

def newton_method(g,guess):
    return try_point(newton_transform(g),guess)

def fixed_point(f,first_guess):
    return try_point(first_guess)

def close_enough(a,b):
    tolerate = 0.001
    return abs(a-b) < tolerate
    #next = float(f(first_guess))

def try_point(f,guess):
        next = float(f(guess))
        print next
        if close_enough(guess,next):return next
        else:return try_point(f,next)

def newton_transform(g):
    return lambda x:(g(x)/deriv(g,x))-x

def deriv(g,a):
    dx = 0.00001
    return (lambda x:(g(x+dx)-g(x))/dx)(a)

def calculate(a,b,c):
    return newton_method(cubic(a,b,c),1.0)

print newton_method(cubic(3,2,1),1.0)