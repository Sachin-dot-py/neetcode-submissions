# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        prev = None
        while curr.next:
            # curr's next will be prev
            # then we go to the actual curr.next
            actual_next = curr.next
            curr.next = prev
            prev = curr
            curr = actual_next
        curr.next = prev
        return curr