# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        
        def dfs(node):
            
            if not node:
                return 
            
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
            
        dfs(root)
        return result

# Breadth First Search
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        result = deque([])
        stack = []
        node = root

        while stack or node:
            while node:
                result.appendleft(node.val)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        
        return list(result)