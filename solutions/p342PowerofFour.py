class Solution(object):
    def isPowerOfFour(self, num):
        tail = bin(num)[3:]
        return num > 0 and len(tail) % 2 == 0 and tail.find('1') == -1
