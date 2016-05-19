from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        q=deque([root])
        res,rem=[],1
        while len(q) > 0:
            new,levelres=0,[]
            while len(q) and rem:
                top = q.popleft()
                rem-=1
                if top == None: continue
                levelres += [top.val]
                q += [top.left, top.right]
                new+=2
            rem=new
            if levelres!=[]: res.append(levelres)
        return res[::-1]