class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.vectors = [v1, v2]
        self.maxlen = max(len(v) for v in self.vectors)
        self.totallen = sum(len(v) for v in self.vectors)
        self.row, self.col = 0, 0

    def next(self):
        r,c = self.row,self.col
        self.row = (self.row + 1) % len(self.vectors); self.col += 0 if self.row else 1
        return self.vectors[r][c]

    def hasNext(self):
        while self.col >= len(self.vectors[self.row]) and self.col <= self.maxlen:
            self.row = (self.row + 1) % len(self.vectors); self.col += 0 if self.row else 1
        return self.col <= self.maxlen and self.maxlen > 0