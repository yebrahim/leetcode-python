class Solution(object):
    def plusOne(self, digits):
        i=len(digits)-1
        while i >= 0:
            digits[i] = (digits[i] + 1) % 10
            if digits[i] > 0: break
            i-=1
        return digits if digits[0] else [1]+digits