class Solution(object):
    def isStrobogrammatic(self, num):
        d=['0','1','-1','-1','-1','-1','9','-1','8','6']
        for i in range((len(num)+1)/2):
            j = len(num)-i-1
            if '1' < num[i] < '6' or num[i] == '7' or num[j] != d[ord(num[i])-48]: return False
        return True