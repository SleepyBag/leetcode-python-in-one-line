# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return (lambda delete_duplicates, *args: delete_duplicates(delete_duplicates, *args))(lambda delete_duplicates, head: head if not head or not head.next else delete_duplicates(delete_duplicates, head.next) if head.val == head.next.val else [head, head.__setattr__('next', delete_duplicates(delete_duplicates, head.next))][0], head)