from collections import deque,defaultdict
class Solution(object):
    
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord); wordList.append(endWord)
        neighbors=defaultdict(set)
        q, visited = deque([(beginWord,1)]), set()
        for w in wordList:
            for i in range(len(w)): neighbors[w[:i] + '.' + w[i+1:]].add(w)
        while len(q):
            w,l = q.popleft()
            if w == endWord: return l
            visited.add(w)
            for i in range(len(w)):
                tmp = w[:i] + '.' + w[i+1:]
                for w2 in neighbors[tmp] - visited:
                    q.append((w2,l+1))
                    visited.add(w2)
        return 0
