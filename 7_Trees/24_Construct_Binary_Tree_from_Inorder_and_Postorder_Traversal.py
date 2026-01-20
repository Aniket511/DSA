class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Build hash map for O(1) lookup of root index in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1  # Start from the end of postorder
        
        def build(in_left, in_right):
            # Base case: no elements to construct the tree
            if in_left > in_right:
                return None
            
            # Get the root value from postorder (from right to left)
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)
            self.post_idx -= 1
            
            # Find root index in inorder
            in_root_idx = inorder_map[root_val]
            
            # Build right subtree first (because we're going right to left in postorder)
            root.right = build(in_root_idx + 1, in_right)
            # Build left subtree
            root.left = build(in_left, in_root_idx - 1)
            
            return root
        
        return build(0, len(inorder) - 1)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        stack = [root]
        inorder_idx = len(inorder) - 1
        
        # Process postorder from right to left (excluding root which is already processed)
        for i in range(len(postorder) - 2, -1, -1):
            node = TreeNode(postorder[i])
            parent = stack[-1]
            
            # If top of stack doesn't match inorder, attach as right child
            if parent.val != inorder[inorder_idx]:
                parent.right = node
            else:
                # Pop nodes until we find where to attach left child
                while stack and stack[-1].val == inorder[inorder_idx]:
                    parent = stack.pop()
                    inorder_idx -= 1
                parent.left = node
            
            stack.append(node)
        
        return root