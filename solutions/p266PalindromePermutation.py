from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        counter=Counter(s)
        return len(filter(lambda x:x[1]%2!=0, counter.items())) <= 1