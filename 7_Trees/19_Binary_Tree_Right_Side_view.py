# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])

        while queue:
            rightSide = None
            qLen = len(queue)

            for i in range(qLen):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                result.append(rightSide.val)
        return result