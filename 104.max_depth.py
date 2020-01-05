# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return (lambda max_depth, *args: max_depth(max_depth, *args))((lambda max_depth, root: 0 if not root else 1 + max(max_depth(max_depth, root.left), max_depth(max_depth, root.right))), root)