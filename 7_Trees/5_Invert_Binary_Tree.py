# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return

            node.left, node.right = node.right, node.left

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return root

# Breadth First Search
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        queue = [root]
        while queue:
            node = queue.pop()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        
        return root