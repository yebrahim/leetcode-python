class Solution(object):
    def isOneEditDistance(self, s, t):
        if len(s) == len(t):
            return len(list(s[c] for c in range(len(s)) if s[c] != t[c])) == 1
        if len(s) < len(t): s,t = t,s
        for i in range(len(s)):
            if t == s[:i] + s[i+1:]: return True
        return False