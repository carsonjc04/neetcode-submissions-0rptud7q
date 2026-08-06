# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            rightSide = None
            qLen = len(q)
            for i in range(qLen):
                cur = q.popleft()
                if cur and cur.left:   
                    q.append(cur.left)
                if cur and cur.right:
                    q.append(cur.right)
                if cur:
                    rightSide = cur.val
            if rightSide:
                res.append(rightSide)
        return res
