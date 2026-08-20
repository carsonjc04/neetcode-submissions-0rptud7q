class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        
        idx = count - n
        if idx == 0:
            return head.next
            
        cur = head
        for i in range(idx - 1):
            cur = cur.next
        
        cur.next = cur.next.next
        return head