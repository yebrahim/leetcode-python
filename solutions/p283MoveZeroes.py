class Solution(object):
    def moveZeroes(self, nums):
        lastpos=0
        for n in nums:
            if n != 0:
                nums[lastpos] = n
                lastpos+=1
        for i in range(lastpos,len(nums)):
            nums[i] = 0