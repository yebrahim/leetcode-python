class Solution(object):
    def isValid(self, s):
        braces = {'}': '{', ')': '(', ']': '['}
        stack = []
        for i in s:
            if i not in braces: stack.append(i)
            elif not len(stack) or braces[i] != stack.pop(): return False
        return not len(stack)