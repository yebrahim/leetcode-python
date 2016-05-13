class Solution(object):
    def isPowerOfThree(self, n):
        while n > 1 and n % 3 == 0:
            n /= 3
        return n == 1