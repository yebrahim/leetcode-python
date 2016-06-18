class MovingAverage(object):

    def __init__(self, size):
        self.w=[]
        self.s = size

    def next(self, val):
        if len(self.w) < self.s: self.w.append(val)
        else: self.w = self.w[1:self.s]+[val]
        return 1.0*sum(self.w)/len(self.w)