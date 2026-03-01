# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        seen = set()

        def dfs(node):
            if not node:
                return False
            
            difference = k - node.val

            if difference in seen:
                return True
            
            seen.add(node.val)

            return dfs(node.left) or dfs(node.right)

        return dfs(root)

from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        queue = deque([root])

        while queue:
            current = queue.popleft()
            if current:    
                difference = k - current.val
                if difference in seen:
                    return True
                seen.add(current.val)
                queue.append(current.left)
                queue.append(current.right)
        return False 

