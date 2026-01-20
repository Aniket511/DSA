# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.diameter = 0

        def dfs(node):
            
            if not node:
                return 0

            leftLength = dfs(node.left)
            rightLength = dfs(node.right)

            self.diameter = max(self.diameter, leftLength + rightLength)

            return 1 + max(leftLength, rightLength)

        dfs(root)
        return self.diameter