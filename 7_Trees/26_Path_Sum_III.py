# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):

        if not root:
            return 0
        
        self.count = 0
        prefixSum = {0 : 1}

        def dfs(node, currentSum):
        
            if not node:
                return
            currentSum += node.val

            self.count += prefixSum.get(currentSum - targetSum, 0)

            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1

            dfs(node.left, currentSum)
            dfs(node.right, currentSum)

            prefixSum[currentSum] -= 1

        dfs(root, 0)
        return self.count
