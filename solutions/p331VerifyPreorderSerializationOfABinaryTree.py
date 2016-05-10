class Solution(object):
    def isValidSerialization(self, preorder):
        p = preorder.split(',')
        i = self.__findSubtree(p)
        while i != -1:
            p[i:i+3] = ['#']
            i = self.__findSubtree(p)
        return p == ['#']
        
    def __findSubtree(self, t):
        if len(t) < 3: return -1
        for i in range(len(t)-2):
            if t[i] != '#' and [t[i+1],t[i+2]] == ['#','#']:
                return i
        return -1