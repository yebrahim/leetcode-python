class Solution(object):
    def filterString(self, s):
        return "".join([e for e in s if e in ['{', '[', '(', '}', ']', ')']]);
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.filterString(s);
        braces = {'}': '{', ')': '(', ']': '['};
        myStack = [];
        for i in s:
            if i in ['{', '(', '[']:
                myStack.append(i);
            else:
                if not len(myStack) or braces[i] != myStack.pop():
                    return False;
        return not len(myStack);