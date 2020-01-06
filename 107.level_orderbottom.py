# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        return (lambda level_order_bottom, *args: level_order_bottom(level_order_bottom, *args))(lambda level_order_bottom, left, right, ans: ans if not True in (available := [i % 2 and right[i // 2] is not None or not i % 2 and left[i // 2] is not None for i in range(2 * len(left))]) else [ans.append([right[i // 2].val if i % 2 else left[i // 2].val for i in range(2 * len(left)) if available[i]]), level_order_bottom(level_order_bottom, [right[i // 2].left if i % 2 else left[i // 2].left for i in range(2 * len(left)) if available[i]], [right[i // 2].right if i % 2 else left[i // 2].right for i in range(2 * len(left)) if available[i]], ans)][-1], [root.left], [root.right], [[root.val]])[::-1] if root is not None else []