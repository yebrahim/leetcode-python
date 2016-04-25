class Solution(object):
    _prices = []
    _profit = 0
    def positiveDelta(self, i):
        diff = self._prices[i] - self._prices[i-1]
        self._profit += max(diff, 0)
    def maxProfit(self, prices):
        self._prices = prices
        list(map(self.positiveDelta, range(1, len(self._prices))))
        return self._profit