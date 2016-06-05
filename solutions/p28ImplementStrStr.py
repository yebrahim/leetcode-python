class Solution(object):
    def strStr(self, haystack, needle):
        if needle=='': return 0
        for i in range(len(haystack)-len(needle)+1):
            j,k=i,0
            while j<len(haystack) and k<len(needle) and haystack[j]==needle[k]: j+=1; k+=1
            if k == len(needle): return i
        return -1