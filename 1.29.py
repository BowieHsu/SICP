#encoding:utf-8
__author__ = 'bowiehsu'
'''过程抽象
   Python无法直接对过程进行抽象，使用Lambda
'''
inc = lambda x:x+1
cube = lambda x:x**3
def sum_q(term,a,next,b):
    if a>b: return 0
    else:return term(a)+sum_q(term,next(a),next,b)
def sum_cubes(a,b):
    return sum_q(cube,a,inc,b)

print sum_cubes(1,10)

def f(x,y):
    return (lambda a,b:x*a**2+y*b+a*b)(1+x*y,y-1)

print f(1,1)