# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return (lambda f, *a: f(f, *a))(lambda check, root: 0 if not root else ((lambda x, y: max(x, y) + 1 if ~x and ~y and abs(x - y) <= 1 else -1)(check(check, root.left), check(check, root.right))), root) >= 0
