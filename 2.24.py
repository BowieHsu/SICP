#encoding:utf-8
__author__ = 'bowiehsu'
'''
假定现在要求值表达式
'''
def deep_reverse(x):
    print x
    if x == None: return x
    if x == ():return x
    else:
        return deep_reverse(x[1]) + deep_reverse(x[0])

test = [1,2,3,4,5]
res = filter(lambda x :x%2 != 0,test)
res2 = map(lambda x:x**2,res)
res3 = sum(res2)
print res,res2,res3