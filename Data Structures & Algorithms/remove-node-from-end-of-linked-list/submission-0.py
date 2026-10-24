# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Slow and fast pointer, but the fast pointer always stays n nodes ahead
        slow, fast = head, head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        # `slow.next` holds the node to be removed
        slow.next = slow.next.next
        
        return head