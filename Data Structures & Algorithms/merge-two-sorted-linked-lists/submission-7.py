# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1 = [1,2,4], list2 = [1,3,5,6,7]
        # [1,1,2,3,4,5]

        # Part1 - Alternate between lists and append smaller values while both lists exist
        # Part2 - Append the rest of remaining list

        new_list = head = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                new_list.next = list2
                list2 = list2.next
            else: 
                new_list.next = list1
                list1 = list1.next
            new_list = new_list.next
        new_list.next = list1 or list2

        return head.next