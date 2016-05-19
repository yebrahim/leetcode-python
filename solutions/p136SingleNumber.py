class Solution(object):
    def singleNumber(self, nums):
        res=0
        for n in nums: res ^= n
        return res