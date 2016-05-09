class NestedIterator(object):
    def __init__(self, nestedList):
        self.flatlist = nestedList

    def next(self):
        e = self.flatlist[0].getInteger()
        self.flatlist = self.flatlist[1:]
        return e

    def hasNext(self):
        if len(self.flatlist) == 0: return False
        while self.flatlist and not self.flatlist[0].isInteger():
            self.flatlist[:1] = [e for e in self.flatlist[0].getList()]
        return len(self.flatlist) > 0
