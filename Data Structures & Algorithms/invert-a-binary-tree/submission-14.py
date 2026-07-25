class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Approach:
        # we have a queue with root. And basically we'd pop the left of queue
        # we have our first node, switch left and right, add to the queue. 
        # because of how the children pointers dont change, we'd still be swithcing those along

        if not root:
            return None
        
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root