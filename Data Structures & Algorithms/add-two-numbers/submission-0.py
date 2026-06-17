# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = None
        cur = None
        carry = 0
        while l1 and l2:
            sumOfUnit = l1.val + l2.val + carry
            carry = sumOfUnit // 10
            if cur:
                cur.next = ListNode(val=sumOfUnit%10)
                cur = cur.next
            else:
                cur = ListNode(val=sumOfUnit%10)
                start = cur

            l1 = l1.next
            l2 = l2.next

        while l1:
            sumOfUnit = l1.val + carry
            carry = sumOfUnit // 10
            cur.next = ListNode(val=sumOfUnit%10)
            cur = cur.next
            l1 = l1.next


        while l2:
            sumOfUnit = l2.val + carry
            carry = sumOfUnit // 10
            cur.next = ListNode(val=sumOfUnit%10)
            cur = cur.next
            l2 = l2.next


        if carry:
            cur.next = ListNode(val=carry)
            
        return start

            

        
