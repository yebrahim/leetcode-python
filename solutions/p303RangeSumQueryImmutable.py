class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.__sums = [nums[0]] if len(nums) > 0 else []
        for n in nums[1:]:
            self.__sums.append(n + self.__sums[-1])

    def sumRange(self, i, j):
        return self.__sums[j] - self.__sums[i - 1] if i > 0 else self.__sums[j]