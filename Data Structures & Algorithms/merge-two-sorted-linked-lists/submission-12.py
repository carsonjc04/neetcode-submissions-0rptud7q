# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        dummy = new

        #0 -> None

        l1 = list1
        l2 = list2

        while l1 and l2:
            v1 = l1.val
            v2 = l2.val

            if v1 > v2:
                new.next = l2
                l2 = l2.next
            else:
                new.next = l1
                l1 = l1.next
            new = new.next

        new.next = l1 or l2

        return dummy.next
