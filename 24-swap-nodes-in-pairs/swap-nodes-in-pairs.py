# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(data):
            if not data or not data.next:
                return
            data.val, data.next.val = data.next.val, data.val
            rec(data.next.next)
        rec(head)
        return head
        