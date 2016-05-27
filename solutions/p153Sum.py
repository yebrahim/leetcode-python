class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        first,r = 0,set()
        while first < len(nums):
            start = first+1; end = len(nums)-1
            while start<end:
                if nums[first] + nums[start] + nums[end] == 0:
                    r.add((nums[first],nums[start],nums[end]))
                    start += 1; end -= 1
                elif nums[first] + nums[start] + nums[end] > 0: end -= 1
                else: start += 1
            first += 1
        return list(r)