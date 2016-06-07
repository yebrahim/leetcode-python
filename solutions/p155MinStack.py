class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minstack = []

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1][0]

    def push(self, v):
        self.stack.append(v)
        if len(self.minstack) == 0 or self.minstack[-1][0] > v:
            self.minstack.append([v,1])
        else:
            self.minstack[-1][1] += 1

    def pop(self):
        if self.minstack[-1][1] > 1:
            self.minstack[-1][1] -= 1
        else:
            self.minstack.pop()
        return self.stack.pop()
