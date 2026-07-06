# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if len(lists) == 0:
        #     return None

        # def merge(list1, list2):
        #     head = list1
        #     prev1 = list1
        #     prev2 = list2
        #     newList = None
        #     end = None


        #     while prev1 != None and prev2 != None:
        #         if prev1.val < prev2.val:
        #             if newList == None:
        #                 newList = prev1
        #                 end = prev1
        #             else:
        #                 end.next = prev1
        #                 end = end.next
        #             prev1 = prev1.next
        #         else:
        #             if newList == None:
        #                 newList = prev2
        #                 end = prev2
        #             else:
        #                 end.next = prev2
        #                 end = end.next
        #             prev2 = prev2.next

                
        #     while prev1 != None:
        #         if newList == None:
        #             newList = prev1
        #             end = prev1
        #         else:
        #             end.next = prev1
        #             end = end.next
        #         prev1 = prev1.next

        #     while prev2 != None:
        #         if newList == None:
        #             newList = prev2
        #             end = prev2
        #         else:
        #             end.next = prev2
        #             end = end.next
        #         prev2 = prev2.next
        
        #     return newList


        # answer = lists[0]
        # print(lists)

        # for i in range(1, len(lists)):
        #     answer = merge(answer, lists[i])
        # return answer


        # allNumbers = []
        # for i in range(len(lists)):
        #     cur_head = lists[i]
        #     while cur_head != None:
        #         allNumbers.append(cur_head.val)
        #         cur_head = cur_head.next


        # allNumbers.sort()
        # head = None
        # tail = None
        # for num in allNumbers:
        #     node = ListNode(val=num)
        #     if head == None:
        #         head = node
        #         tail = node
        #     else:
        #         tail.next = node
        #         tail = tail.next

        # return head


        # def merge(list1, list2):
        #     p1 = list1
        #     p2 = list2
        #     head = ListNode()
        #     prev = head

        #     while p1 and p2:
        #         if p1.val < p2.val:
        #             prev.next = p1
        #             prev = prev.next
        #             p1 = p1.next
        #         else:
        #             prev.next = p2
        #             prev = prev.next
        #             p2 = p2.next

        #     while p1:
        #         prev.next = p1
        #         prev = prev.next
        #         p1 = p1.next

        #     while p2:
        #         prev.next = p2
        #         prev = prev.next
        #         p2 = p2.next

        #     return head.next

        # if len(lists) == 0:
        #     return None

        # answer = lists[0]

        # for i in range(1, len(lists)):
        #     answer = merge(answer, lists[i])
        # return answer
        
        minheap = []
        n = len(lists)
        for i in range(n):
            if lists[i]:
                heapq.heappush(minheap, (lists[i].val, i,lists[i]))

        head = ListNode()
        tail = head
        while minheap:
            val, i, node = heapq.heappop(minheap)
            tail.next = node
            tail = tail.next
            nextNode = node.next
            if nextNode != None:
                heapq.heappush(minheap, (nextNode.val, i, nextNode))

        return head.next


        
        