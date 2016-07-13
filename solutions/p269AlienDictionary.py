from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        if len(words) == 1: return words[0]
        d=defaultdict(set)
        visited = [-2]*26 # -2 doesn't exist, -1: not visited, 0: visiting, 1: visited
        for w1,w2 in zip(*[words,words[1:]]):
            for c in w1+w2: visited[ord(c)-ord('a')] = -1
            for i in range(min(len(w1),len(w2))):
                if w1[i] != w2[i]: d[w1[i]].add(w2[i]); break
        self.order=''

        def dfs(s):
            if visited[ord(s)-ord('a')] == 0: return False # cycle
            if visited[ord(s)-ord('a')] == 1: return True
            visited[ord(s)-ord('a')] = 0
            for n in d[s]:
                if not dfs(n): return False
            visited[ord(s)-ord('a')] = 1
            self.order+=s
            return True
            
        for i in range(26):
            if visited[i] == -1 and not dfs(chr(ord('a')+i)): return ''
        return self.order[::-1]