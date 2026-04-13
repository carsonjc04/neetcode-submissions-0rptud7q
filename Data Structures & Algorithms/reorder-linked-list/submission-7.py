# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5, 6] -> [0, 6, 1, 5, 2, 4, 3]
        # [0,1,2,3] [4,5,6] -> [6,5,4]. -> [0,6,1, 5, 2, 4, 3]

        fast = slow = head
        # [0, 1, 2, 3, 4, 5, 6]
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        first = head
        # second None <-[4,5,6]
        # first = [0,1,2,3]
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        
