# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, currentDepth):
            if not node:
                return 0
            left_depth = dfs(node.left, currentDepth + 1)
            right_depth = dfs(node.right, currentDepth + 1)

            return max(currentDepth, left_depth, right_depth)

        return dfs(root, 1)

# Breadth First Search
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = deque([[root, 1]])
        maxDepth = float("-infinity")
        while queue:
            current, currentDepth = queue.popleft()
            maxDepth = max(maxDepth, currentDepth)
            if current.left:
                queue.append((current.left, currentDepth + 1))            
            if current.right:
                queue.append((current.right, currentDepth + 1))        

        return maxDepth