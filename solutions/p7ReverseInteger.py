class Solution(object):
    def reverse(self, x):
        r = int(str(x)[::-1] if x >= 0 else '-'+str(-x)[::-1])
        return r if -(2**31-1) < r < (2**31-1) else 0