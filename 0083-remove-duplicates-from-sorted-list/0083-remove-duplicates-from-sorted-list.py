# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev, curr = head, head.next
        
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        
        return head
        