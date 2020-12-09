class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return False if root is None else (lambda f, *args: f(f, *args))((lambda f, root, sum: (root is not None) and ((root.left is None and root.right is None and sum == root.val) or (f(f, root.left, sum - root.val)) or (f(f, root.right, sum - root.val)))), root, sum)
