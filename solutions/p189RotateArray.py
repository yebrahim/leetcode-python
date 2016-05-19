class Solution(object):
    def rotate(self, nums, k):
        k = k%len(nums) * -1
        nums[:]=nums[k:]+nums[:k]