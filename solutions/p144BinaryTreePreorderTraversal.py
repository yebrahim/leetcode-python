class Solution(object):
    def preorderTraversal(self, root):
        s,res=[],[]
        while root or len(s):
            while root:
                res.append(root.val)
                s.append(root)
                root = root.left
            root = s.pop()
            root = root.right
        return res