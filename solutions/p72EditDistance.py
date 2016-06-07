class Solution(object):
    def __init__(self):
        self.d = {}
    def minDistance(self, A, B):
        if (len(A), len(B)) in self.d: return self.d[(len(A),len(B))]
        if len(A) == 0: r = len(B)
        elif len(B) == 0: r = len(A)
        elif A[0] == B[0]: r = self.minDistance(A[1:], B[1:])
        else: r = 1 + min(self.minDistance(A[1:], B), self.minDistance(A, B[1:]), self.minDistance(A[1:], B[1:]))
        self.d[(len(A), len(B))] = r
        return r