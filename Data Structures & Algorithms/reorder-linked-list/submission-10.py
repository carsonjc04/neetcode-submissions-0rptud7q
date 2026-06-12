# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        


        # first = 0,1,2,3
        # second = 4, 5, 6 -> 6, 5, 4
        # final = 0, 6,