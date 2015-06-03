#encoding:utf-8
__author__ = 'bowiehsu'
'''过程作为一般性的方法
'''
import math
f = lambda x: x**3-x*2-3

def close_enough(x,y):
    if abs(x-y) < 0.001:return True
    else:return False

def search(f,neg,pos):

    mid = float((neg+pos)/2)
    #print neg,pos,mid
    if close_enough(neg,pos):return mid
    mid_value = f(mid)
    if mid_value > 0: return search(f,neg,mid)
    elif mid_value < 0:return search(f,mid,pos)
    elif mid_value == 0:return mid


def half_interval_method(f,a,b):
    a_value = f(a)
    b_value = f(b)

    if a_value < 0 and b_value > 0:
            return search(f,a,b)
    elif a_value > 0 and b_value < 0:
            return search(f,b,a)
    else:print "Error Value"

#print half_interval_method(f,1,2)
print half_interval_method(f,1,2)

'''找出函数的不动点
'''
tolerate = 0.00001
def fixed_point(f,first_guess):
    def close_enough(a,b):return abs(a-b) < tolerate
    #next = float(f(first_guess))
    def try_point(guess):
        next = float(f(guess))
        if close_enough(guess,next):return next
        else:return try_point(next)
    return try_point(first_guess)

print fixed_point(lambda x: 1 +1.0)