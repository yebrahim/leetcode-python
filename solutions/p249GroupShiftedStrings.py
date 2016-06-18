from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        d=defaultdict(list)
        for s in strings:
            shift = ord(s[0]) - ord('a')
            _s = ''.join(chr((ord(c)-shift+26)%26) for c in s)
            d[_s].append(s)
        return d.values()