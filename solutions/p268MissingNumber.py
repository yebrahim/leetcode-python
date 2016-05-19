class Solution(object):
    def missingNumber(self, nums):
        l=len(nums)
        return l*(l+1)/2 - sum(nums)