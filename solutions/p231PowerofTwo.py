class Solution(object):
    def isPowerOfTwo(self, n):
        return n >= 0 and bin(n).count('1') == 1