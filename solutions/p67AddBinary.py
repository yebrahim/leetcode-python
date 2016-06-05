class Solution(object):
    def addBinary(self, a, b):
        a=a.zfill(max(len(a),len(b)))[::-1]
        b=b.zfill(max(len(a),len(b)))[::-1]
        c,carry='',0
        for i in range(len(a)):
            t=int(a[i])+int(b[i])+carry
            c,carry = c+str(t%2),t > 1
        if carry: c += '1'
        return c[::-1]