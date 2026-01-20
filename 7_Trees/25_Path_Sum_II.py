# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)

            if node.left is None and node.right is None and remaining == node.val:
                result.append(path[:])
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)

            path.pop()

        dfs(root, targetSum, [])
        return result


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []

        result = []
        stack = [(root, targetSum, [])]

        while stack:
            node, remaining, path = stack.pop()
            path = path + [node.val]

            if node.left is None and node.right is None and remaining == node.val:
                result.append(path)
            if node.right:
                stack.append((node.right, remaining - node.val, path))
            if node.left:
                stack.append((node.left, remaining - node.val, path))

        return result

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []
        
        result = []
        queue = deque([(root, [root.val], root.val)])  # (node, path, current_sum)
        
        while queue:
            node, path, current_sum = queue.popleft()
            
            # Check if it's a leaf with target sum
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path)
            
            # Add children to queue
            if node.left:
                queue.append((node.left, path + [node.left.val], current_sum + node.left.val))
            if node.right:
                queue.append((node.right, path + [node.right.val], current_sum + node.right.val))
        
        return result