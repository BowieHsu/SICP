#encoding:utf-8
__author__ = 'bowiehsu'
def make_rat(n,d):
    return (n,d)

def number(x):
     return x[0]

def denom(x):
   return x[1]

def add_rat(x,y):
    return make_rat(number(x)*denom(y)+number(y)*denom(x),denom(x)*denom(y))

print add_rat((1,1),(2,1))