class Solution(object):
    def twoSum(self, numbers, target):
        start,end=0,len(numbers)-1
        while start < end:
            sum=numbers[start]+numbers[end]
            if sum == target: return [start+1, end+1]
            elif sum < target: start += 1
            else: end -= 1