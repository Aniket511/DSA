# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        else:
            if self.isSametree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSametree(self, node1, node2):
        if not node1 and not node2:
            return True
        elif node1 and node2 and node1.val == node2.val:
            return self.isSametree(node1.left, node2.left) and self.isSametree(node1.right, node2.right)
        else:
            return False