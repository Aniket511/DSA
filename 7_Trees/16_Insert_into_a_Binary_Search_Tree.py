# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root: 
            return TreeNode(val)
        
        new_node = TreeNode(val)
        node = root
        
        while node:
        
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    break
        
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    break
        
        return root