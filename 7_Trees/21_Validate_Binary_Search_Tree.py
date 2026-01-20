# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(leftVal, node, rightVal):

            if not node:
                return True

            elif not leftVal < node.val < rightVal:
                return False

            return dfs(leftVal, node.left, node.val) and dfs(node.val, node.right, rightVal)

        return dfs(float('-infinity'), root, float('infinity'))
        

class Solution:
    def isValidBST(self, root):

        queue = deque()
        queue.append([float('-infinity'), root, float('infinity')])
        while queue:

            leftVal, node, rightVal = queue.popleft()

            if not leftVal < node.val < rightVal:
                return False
            if node.left:
                queue.append([leftVal, node.left, node.val])
            if node.right:
                queue.append([node.val, node.right, rightVal])
            
        return True