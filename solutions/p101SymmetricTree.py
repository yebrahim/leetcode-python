from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        remaining=1
        q=deque([root])
        while len(q) > 0:
            new,level=0,[]
            while len(q) and remaining:
                node = q.popleft()
                remaining-=1
                level+=[node.val if node else None]
                if not node: continue
                q+=[node.left, node.right]
                new+=2
            remaining=new
            if level != level[::-1]: return False
        return True