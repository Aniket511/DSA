class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build hash map for O(1) lookup of root index in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0  # Start from the beginning of preorder
        
        def build(in_left, in_right):
            # Base case: no elements to construct the tree
            if in_left > in_right:
                return None
            
            # Get the root value from preorder (from left to right)
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Find root index in inorder
            in_root_idx = inorder_map[root_val]
            
            # Build left subtree first (because we're going left to right in preorder)
            root.left = build(in_left, in_root_idx - 1)
            # Build right subtree
            root.right = build(in_root_idx + 1, in_right)
            
            return root
        
        return build(0, len(inorder) - 1)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_idx = 0
        
        # Process preorder from left to right (excluding root which is already processed)
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            parent = stack[-1]
            
            # If top of stack doesn't match inorder, attach as left child
            if parent.val != inorder[inorder_idx]:
                parent.left = node
            else:
                # Pop nodes until we find where to attach right child
                while stack and stack[-1].val == inorder[inorder_idx]:
                    parent = stack.pop()
                    inorder_idx += 1
                parent.right = node
            
            stack.append(node)
        
        return root