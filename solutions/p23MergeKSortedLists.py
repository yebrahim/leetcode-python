from heapq import *
class Solution(object):
    def mergeKLists(self, lists):
        q=[]
        res=r=ListNode(0)
        for i,l in enumerate(lists):
            if l:
                heappush(q, (l.val,i))
                l = l.next
        while len(q):
            v,i = heappop(q)
            r.next = ListNode(v)
            r=r.next
            lists[i] = lists[i].next
            if lists[i]:
                heappush(q, (lists[i].val,i))
        return res.next