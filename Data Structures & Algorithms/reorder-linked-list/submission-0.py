import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0
        node = head
        while node != None:
            n += 1
            node = node.next

        half = math.ceil(n/2)

        node = head
        left = None
        for i in range(half):
            left = node 
            node = node.next
            # print(node.val, left.val)

        left.next = None
        list1 = head
        list2 = node
        # print(n, half)
        # print(list1)
        # print()
        # print(list2)

        # Reversing list2

        left = None
        center = list2
        # right = list2.next
        while center != None:
            right = center.next
            center.next = left
            left = center
            center = right

        list2 = left
        # print(list1)
        # print()
        # print(list2)
        while list2 != None:
            temp = list1.next
            list1.next = list2
            list2 = list2.next
            list1.next.next = temp
            list1 = temp
            

