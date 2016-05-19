class Queue(object):
    def __init__(self):
        self.s1,self.s2=[],[]
        pass
    
    def push(self, x):
        for i in range(len(self.s2)): self.s1.append(self.s2.pop())
        self.s1.append(x)

    def pop(self):
        for i in range(len(self.s1)): self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        return self.s1[0] if len(self.s1) else self.s2[-1]

    def empty(self):
        return len(self.s1) + len(self.s2) == 0