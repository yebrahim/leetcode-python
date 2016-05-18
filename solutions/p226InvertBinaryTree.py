class Solution(object):
    def invertTree(self, root):
        if root == None: return
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root