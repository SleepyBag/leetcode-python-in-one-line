class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return 0 if root is None else (lambda f, root: f(f, root))((lambda f, root: 1 if root is not None and root.left is None and root.right is None else min(f(f, root.left), f(f, root.right)) + 1 if root is not None else inf), root)
