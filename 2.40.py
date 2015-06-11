#encoding:utf-8
__author__ = 'bowiehsu'

def accumulate(x):
    res = []
    for i in range(x):
        for j in range(i):
            res.append([i,j])
    print res
    res2 = filter(lambda i:prime_sum(i),res)
    return res2

#根据费马小定理，a**n%n == a，则n为素数
def fast_prime(n):
    for a in range(n):
        if (a**n)%n != a:return False
    return True

def prime_sum(pair):
    return fast_prime(pair[0] + pair[1])

def unique_pairs(x):
    pass

print accumulate(6)
print fast_prime(7)