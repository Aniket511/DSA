# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, current_num):
            if not node:
                return 0
            
            # Build the number for current path
            current_num = current_num * 10 + node.val
            
            # If it's a leaf, return the number
            if not node.left and not node.right:
                return current_num
            
            # Otherwise, sum the results from left and right subtrees
            return dfs(node.left, current_num) + dfs(node.right, current_num)
        
        return dfs(root, 0)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_sum = 0
        queue = deque([(root, 0)])  # (node, current_number)
        
        while queue:
            node, current_num = queue.popleft()
            current_num = current_num * 10 + node.val
            
            # If it's a leaf, add to total sum
            if not node.left and not node.right:
                total_sum += current_num
            
            # Add children to queue
            if node.left:
                queue.append((node.left, current_num))
            if node.right:
                queue.append((node.right, current_num))
        
        return total_sum