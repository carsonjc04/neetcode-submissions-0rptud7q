"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OldToCopy = defaultdict(lambda: Node(0))
        OldToCopy[None] = None

        cur = head
        while cur:
            OldToCopy[cur].val = cur.val
            OldToCopy[cur].next = OldToCopy[cur.next]
            OldToCopy[cur].random = OldToCopy[cur.random]
            cur = cur.next
        return OldToCopy[head]