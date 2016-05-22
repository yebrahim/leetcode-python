import math
class Solution(object):
    __mem={}
    __perfectSquares=None
    def __findPerfectSquares(self, n):
        i,res=2,[1]
        while i**2 <= n:
            res.append(i**2)
            i+=1
        return res
        
    def numSquares(self, n):
        if not self.__perfectSquares: self.__perfectSquares = self.__findPerfectSquares(n)
        if int(math.sqrt(n))**2 == n: return 1
        if n in self.__mem: return self.__mem[n]
        ways=[]
        for s in self.__perfectSquares:
            if s > n: break
            ways.append(self.numSquares(n-s)+1)
        self.__mem[n]=min(ways)
        return self.__mem[n]
        
s=Solution()
print(s.numSquares(11))