# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        self.longestPath = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            leftLength = 0
            rightLength = 0

            if node.left and node.left.val == node.val:
                leftLength = left + 1

            if node.right and node.right.val == node.val:
                rightLength = right + 1

            self.longestPath = max(self.longestPath, leftLength + rightLength)

            return max(leftLength, rightLength)

        dfs(root)
        return self.longestPath
