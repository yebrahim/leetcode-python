class Solution(object):
    def productExceptSelf(self, nums):
        mults=[1]*len(nums)
        for i in range(1,len(nums)):
            mults[i] = nums[i-1]*mults[i-1]
        for i in range(len(nums)-1, 0, -1):
            mults[i] *= mults[0]
            mults[0] *= nums[i]
        return mults

    def productExceptSelf2(self, nums):
        forward=[1]*len(nums)
        backward=[1]*len(nums)
        for i in range(1,len(nums)):
            forward[i] = nums[i-1]*forward[i-1]
        for i in range(len(nums)-2, -1, -1):
            backward[i] = backward[i+1]*nums[i+1]
        for i in range(len(nums)):
            nums[i] = backward[i]*forward[i]
        return nums