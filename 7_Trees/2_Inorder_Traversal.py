# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        
        result = []

        def dfs(node):

            if not node:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return result

# Breadth First Search
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        
        if not root:
            return []

        result = []
        stack = []
        node = root

        while stack or node:

            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result
