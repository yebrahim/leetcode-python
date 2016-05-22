class Solution(object):
    def merge(self, intervals):
        if intervals == []: return []
        intervals.sort(key=lambda x:x.start)
        current,res=intervals[0],[]
        for i in intervals[1:]:
            if i.start > current.end:
                res.append(current)
                current = i
            else: current.end = max(current.end,i.end)
        res.append(current)
        return res