import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = collections.Counter(nums)
        s = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return list(i for i,c in s[:k])

s = Solution()
print(s.topKFrequent([1,1,1,1,2,2,2,3,3,3,3,3,3], 2))