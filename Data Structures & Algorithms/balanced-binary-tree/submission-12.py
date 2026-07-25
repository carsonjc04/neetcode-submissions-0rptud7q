# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
     # Left subtree = 2 while right = 0, FAIL
     # DFS checking each node. abs(cur -= dfs) > 1: False
     # 

        def heightCheck(root):

            if not root:
                return [True, 0]
            
            left, right = heightCheck(root.left), heightCheck(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        return heightCheck(root)[0]
        
        # [True, 0]   