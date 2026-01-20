# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def dfs(node):

            if not node:
                return 
            
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

# Breadth First Search
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            current = stack.pop()
            current = current.right

        return result