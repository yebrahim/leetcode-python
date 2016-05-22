class Solution(object):
    def longestConsecutive(self, root):
        self.longestFound=0
        def dfs(node):
            if not node: return 0
            l,r = dfs(node.left),dfs(node.right)
            l = l+1 if node.left and node.val+1==node.left.val else 1
            r = r+1 if node.right and node.val+1==node.right.val else 1
            self.longestFound = max(self.longestFound, l, r)
            return max(l,r)
        dfs(root)
        return self.longestFound