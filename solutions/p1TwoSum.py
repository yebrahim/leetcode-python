class Solution(object):
    def twoSum(self, nums, target):
        sortednums = sorted((n,i) for i,n in enumerate(nums))
        start,end = 0,len(nums)-1
        while True:
            if sortednums[start][0] + sortednums[end][0] > target: end -= 1
            elif sortednums[start][0] + sortednums[end][0] < target: start += 1
            else: return [sortednums[start][1], sortednums[end][1]]