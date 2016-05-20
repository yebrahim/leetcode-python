class Solution(object):
    def kthSmallest(self, root, k):
        s=[]
        while root or len(s):
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            if k == 1: return root.val
            else: k -= 1
            root = root.right