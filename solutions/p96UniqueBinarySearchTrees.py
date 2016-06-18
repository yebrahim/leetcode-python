class Solution(object):
    def __init__(self):
        self.dp = {1:1, 2:2}
    def numTrees(self, n):
        if n <= 0: return 1
        if n in self.dp: return self.dp[n]
        count=0
        for i in range(n):
            count += self.numTrees(n-i-1) * self.numTrees(i)
        self.dp[n] = count
        return count
