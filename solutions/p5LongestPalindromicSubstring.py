class Solution(object):
    def longestPalindrome(self, s):
        start,maxlen = 0,1
        i,l=0,len(s)
        if l<2: return s
        while i < l:
            if l - i <= maxlen / 2: break
            j=k=i
            while k<l-1 and s[k+1]==s[k]: k+=1
            i=k+1
            while j>=0 and k<l and s[j]==s[k]: j-=1; k+=1
            if k-j-1 > maxlen: maxlen,start = k-j-1,j+1
        return s[start:start+maxlen]