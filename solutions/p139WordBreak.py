class Solution(object):
    def wordBreak(self, s, wordDict):
        d = {}
        wordLen=sorted(set(map(len,wordDict)))
        def wordBreakHelper(s):
            if s in wordDict: d[s]=True; return True
            if s in d: return d[s]
            if len(s) == 1 and s not in wordDict: d[s]=False; return False
            for i in wordLen:
                if s[:i] in wordDict and wordBreakHelper(s[i:]):
                    d[s]=True; return True
            d[s]=False; return False
        return wordBreakHelper(s)