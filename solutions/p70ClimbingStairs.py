class Solution(object):
    def climbStairs(self, n):
        ways,next=1,1
        for i in range(n):
            ways,next = next,ways+next
        return ways