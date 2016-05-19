class Solution(object):
    def isHappy(self, n):
        if n <= 0: return False
        history=set()
        while n != 1 and n not in history:
            history.add(n)
            n = sum([int(c)**2 for c in str(n)])
        return n == 1