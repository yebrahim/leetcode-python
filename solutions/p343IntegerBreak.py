class Solution(object):
    def integerBreak(self, n):
        if n in [2,3]: return n - 1
        res = 1
        while(n - 3 > 1):
            n -= 3
            res *= 3
        while(n - 2 > 1):
            n -= 2
            res *= 2
        return res * n