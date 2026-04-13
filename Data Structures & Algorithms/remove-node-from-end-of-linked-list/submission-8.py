# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode(0, head)
        dummy = node
        right = head
        while n:
            head = head.next
            n -= 1
        
        while head:
            node = node.next
            head = head.next
        node.next = node.next.next
        return dummy.next