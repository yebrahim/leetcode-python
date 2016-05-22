class Solution(object):
    def summaryRanges(self, nums):
        if nums == []: return []
        if len(nums) == 1: return [str(nums[0])]
        res=[]
        start=nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]+1:
                res.append(str(start) + '->' + str(nums[i-1]) if start != nums[i-1] else str(start))
                start = nums[i]
        res.append(str(start) + '->' + str(nums[-1]) if start != nums[-1] else str(start))
        return res