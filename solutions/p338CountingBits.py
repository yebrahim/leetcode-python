class Solution(object):
    def countBits(self, num):
        ar = [0]
        while len(ar) <= num:
            ar += [e + 1 for e in ar[:num+1 - len(ar)]]
        return ar[:num+1]