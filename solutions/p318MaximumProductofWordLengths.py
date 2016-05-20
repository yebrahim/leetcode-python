class Solution(object):
    def maxProduct(self, words):
        nums,maxlen=[],0
        for w in words:
            n=0
            for l in w: n |= 1 << (ord(l)-ord('a'))
            nums.append(n)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]&nums[j]==0: maxlen=max(maxlen, len(words[i])*len(words[j]))
        return maxlen
