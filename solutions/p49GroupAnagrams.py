from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        def hashit(s):
            r=1
            for c in s: r*=primes[ord(c)-ord('a')]
            return r
        d=defaultdict(list)
        for s in strs:
            d[hashit(s)].append(s)
        return [v for v in d.values()]