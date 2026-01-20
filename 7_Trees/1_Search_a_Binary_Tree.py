# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Depth First Search
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        def dfs(node):
            if not node:
                return None
            
            if node.val == val:
                return node
            elif node.val > val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        return dfs(root)


# Iterative Depth First Search
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return None

        stack = [root]

        while stack:
            current = stack.pop()
            if current.val == val:
                return current
            elif current.val > val:
                if current.left:
                    stack.append(current.left)
            else:
                if current.right:
                    stack.append(current.right)

        return None


# Breadth First Search
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return None

        queue = deque([root])

        while queue:
            current = queue.popleft()
            if current.val == val:
                return current
            elif current.val > val:
                if current.left:
                    queue.append(current.left)
            else:
                if current.right:
                    queue.append(current.right)

        return None