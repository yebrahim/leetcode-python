import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = collections.Counter(nums)
        s = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return list(i for i,c in s[:k])
