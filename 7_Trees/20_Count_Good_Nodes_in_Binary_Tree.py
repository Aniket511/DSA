

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node, max_so_far):
            if not node:
                return
            
            # Check if current node is good
            if node.val >= max_so_far:
                self.count += 1
            
            # Update max for children
            new_max = max(max_so_far, node.val)
            
            # Traverse children
            dfs(node.left, new_max)
            dfs(node.right, new_max)
        
        dfs(root, root.val)
        return self.count

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0
        stack = [(root, root.val)]  # (node, max_so_far)
        
        while stack:
            node, max_so_far = stack.pop()
            
            # Check if current node is good
            if node.val >= max_so_far:
                self.count += 1
            
            # Update max for children
            new_max = max(max_so_far, node.val)
            
            # Add children to stack
            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))
        
        return self.count

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0
        queue = deque([(root, root.val)])  # (node, max_so_far)
        
        while queue:
            node, max_so_far = queue.popleft()
            
            # Check if current node is good
            if node.val >= max_so_far:
                self.count += 1
            
            # Update max for children
            new_max = max(max_so_far, node.val)
            
            # Add children to queue
            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))
        
        return self.count