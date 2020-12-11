# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return (lambda same, *args: same(same, *args))(lambda same, a, b: True if a is b else False if type(a) is not type(b) or a.val != b.val else same(same, a.left, b.right) and same(same, a.right, b.left), root.left, root.right) if root is not None else True