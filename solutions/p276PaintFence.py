class Solution(object):
    def numWays(self, n, k):
        if not n: return 0
        if n <= 2: return k**n
        diff = k*(k-1)
        same = k
        for i in range(n-2):
            same,diff = diff,(same+diff)*(k-1)
        return same+diff