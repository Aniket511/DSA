# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        NOT_COVERED = 0   # Node is not monitored and has no camera
        HAS_CAMERA = 1    # Node has a camera installed on it
        COVERED = 2       # Node is monitored by a camera

        self.cameras = 0
        
        def dfs(node):
            if not node:
                return COVERED  # Null nodes are considered covered
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If a child is not covered, we must put a camera here
            if left == NOT_COVERED or right == NOT_COVERED:
                self.cameras += 1
                return HAS_CAMERA
            
            # If child has camera, this node is automatically covered
            if left == HAS_CAMERA or right == HAS_CAMERA:
                return COVERED
            
            # Otherwise, this node becomes NOT_COVERED
            return NOT_COVERED
        
        # If root is NOT_COVERED, place a camera here
        if dfs(root) == NOT_COVERED:
            self.cameras += 1
        
        return self.cameras