class Solution(object):
    def addDigits(self, num):
        return num%9 if num%9 or num==0 else 9