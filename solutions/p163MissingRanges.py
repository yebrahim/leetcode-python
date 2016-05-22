class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        nums = [lower-1] + nums + [upper+1]
        res=[]
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 2: res.append(str(nums[i]-1))
            elif nums[i] - nums[i-1] > 2: res.append(str(nums[i-1]+1) + '->' + str(nums[i]-1))
        return res