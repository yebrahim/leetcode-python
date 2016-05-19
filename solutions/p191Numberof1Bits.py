class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')
    def hammingWeight2(self, n):
        sum=0
        while n:
            sum += n & 1
            n >>= 1
        return sum