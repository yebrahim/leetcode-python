class Solution(object):
    def rob(self, root):
        sol = self.__rob(root)
        return max(sol[0], sol[1])

    def __rob(self, root):
        if root is None: return [0, 0]
        if root.left is None and root.right is None:
            return [root.val, 0]
        left = self.__rob(root.left)
        right = self.__rob(root.right)
        sol1 = root.val + left[1] + right[1]
        sol2 = left[0] + right[0]
        return [max(sol1,sol2), sol2]