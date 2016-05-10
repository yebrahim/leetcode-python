class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd,even = head,head.next
        prev,one,two = odd,odd,even
        while one.next or two.next:
            one.next = one.next.next if one.next else None
            two.next = two.next.next if two.next else None
            if one.next: one=one.next
            if two.next: two=two.next
            prev = one
        prev.next = even
        return odd
