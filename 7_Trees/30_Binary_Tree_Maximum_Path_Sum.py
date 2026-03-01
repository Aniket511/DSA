# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maximumSum = float("-infinity")

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)  
            right = max(dfs(node.right), 0)  

            currentSum = node.val + left + right

            self.maximumSum = max(self.maximumSum, currentSum)

            return node.val + max(left, right)

        dfs(root)

        return self.maximumSum