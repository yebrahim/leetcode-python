class PeekingIterator(object):
    def __init__(self, iterator):
        self.toprocess=None
        self.it = iterator

    def peek(self):
        if not self.toprocess:
            self.toprocess=self.it.next()
        return self.toprocess

    def next(self):
        if self.toprocess:
            x=self.toprocess
            self.toprocess = None
            return x
        else:
            return self.it.next()

    def hasNext(self):
        return self.toprocess!=None or self.it.hasNext()
