from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        xor = reduce(lambda x,y:x^y, nums)
        diffbit = xor & -xor
        first=second=0
        for n in nums:
            if n&diffbit: first ^= n
            else: second ^= n
        return [first,second]
        
    def singleNumber2(self, nums):
        freq=defaultdict(int)
        for n in nums: freq[n]+=1
        return [n for n in freq if freq[n]==1]