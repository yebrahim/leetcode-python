class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry,r=0,[]
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            r.append(carry%10)
            carry/=10
        return r