class Solution(object):
    def inorderTraversal(self, root):
        s,res=[],[]
        while root or len(s):
            while root:
                s.append(root)
                root=root.left
            root=s.pop()
            res.append(root.val)
            root=root.right
        return res