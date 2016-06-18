class Solution(object):
    def __init__(self):
        self.mindiff, self.minval = None, None
    def closestValue(self, root, target):
        if not root: return
        if root.val == target: self.minval = root.val; return
        if not self.mindiff or self.mindiff > math.fabs(target-root.val):
            self.mindiff, self.minval = math.fabs(target-root.val), root.val
        self.closestValue(root.right if target>root.val else root.left, target)
        return self.minval