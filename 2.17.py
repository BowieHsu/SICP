#encoding:utf-8
__author__ = 'bowiehsu'
'''
练习2.17
'''
def last_pair(x):
    if x == None:return None
    elif x[1] == None:return x
    else:return last_pair(x[1])

x = (23,(72,(149,(34,None))))
print x[1]
print last_pair(x)

'''
练习2.18
'''
def reverse(x):
    l = len(x)
    #print x[:l]
    if x == None:return None
    if x == []:return x
    else:
        return [x[-1]]+reverse(x[0:l-1])

print reverse([1,2,3,4])

'''
练习2.19
兑换零钱计数程序
'''
def cc(count,coin_value):
    pass

'''
辗转相除法求最大公约数
'''
def gcd(a,b):
    if b == 0:return a
    else:return gcd(b,a%b)

print gcd(196,5)

