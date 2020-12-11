# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return (lambda same, *args: same(same, *args))(lambda same, a, b: True if a is b else False if type(a) is not type(b) or a.val != b.val else same(same, a.left, b.left) and same(same, a.right, b.right), p, q)