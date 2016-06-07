class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 0: return 0
        neg=pos=maxp = nums[0]
        for n in nums[1:]:
            neg,pos = min(n, neg*n, pos*n), max(n, neg*n, pos*n)
            maxp = max(maxp, pos)
        return maxp