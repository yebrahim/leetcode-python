class Solution(object):
    def deleteDuplicates(self, head):
        savedhead = head
        while head and head.next:
            if head.val == head.next.val: head.next = head.next.next
            else: head = head.next
        return savedhead