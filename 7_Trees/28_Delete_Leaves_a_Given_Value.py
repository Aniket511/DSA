# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):

            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.left is None and node.right is None and node.val == target:
                return None

            return node

        return dfs(root)

 
from collections import deque
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        queue = deque([root])
        nodes = deque([])

        while queue:
            current = queue.popleft()
            if current:
                nodes.appendleft(current)
                queue.appendleft(current.right)
                queue.appendleft(current.left)

        for node in nodes:
            if node.left and node.left.left == node.left.right == None and node.left.val == target:
                node.left = None
            if node.right and node.right.left == node.right.right == None and node.right.val == target:
                node.right = None
        
        if not node.left and not node.right and node.val == target:
            return None

        return root