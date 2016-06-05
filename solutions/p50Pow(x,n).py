class Solution(object):
    def myPow(self, x, n):
        res,e = 1,abs(n)
        while e:
            if e&1 == 1: res *= x
            x *= x
            e /= 2
        return res if n >= 0 else 1.0/res