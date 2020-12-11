class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        return (checker := (lambda head, s: None if head is None else head if id(head) in s else checker(head.next, s)))(headB, (collector := (lambda head: set() if head is None else ((s := collector(head.next)).add(id(head)), s)[-1]))(headA))
