import functools
class Solution(object):
    def maxProfit(self, prices):
        return functools.reduce(lambda x,y:x + max(prices[y] - prices[y-1], 0), range(0, len(prices))) if len(prices) > 1 else 0
