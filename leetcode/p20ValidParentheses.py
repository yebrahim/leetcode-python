class Solution(object):
    def isValid(self, s):
        s = re.sub(r'[^\{\(\[\]\)\}}]', '', s);
        braces = {'}': '{', ')': '(', ']': '['};
        myStack = [];
        for i in s:
            if i in braces:
                if not len(myStack) or braces[i] != myStack.pop():
                    return False;
            else:
                myStack.append(i);
        return not len(myStack);
        