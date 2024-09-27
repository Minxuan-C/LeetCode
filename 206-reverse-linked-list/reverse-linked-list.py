# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rec(data, past):
            if not data:
                return past
            next_temp = data.next
            data.next = past
            past = data
            return rec(next_temp, past) 
        
        return rec(head, None)