class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return 0 if root is None else 1 if root.left is None and root.right is None else min(self.minDepth(root.left) if root.left is not None else inf, self.minDepth(root.right) if root.right is not None else inf) + 1
