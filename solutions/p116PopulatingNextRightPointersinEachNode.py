class Solution(object):
    def connect(self, root, nextleft=None):
        if not root or not root.left:
            return
        root.left.next = root.right
        if root.next: root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
