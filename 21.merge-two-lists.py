# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return (lambda merge, *args: merge(merge, *args)[0])(lambda merge, head1, head2: ((head2, head2.__setattr__('next', merge(merge, head1, head2.next)[0])) if head1.val >= head2.val else merge(merge, head2, head1)) if head1 and head2 else ((head1 or head2), None), l1, l2)