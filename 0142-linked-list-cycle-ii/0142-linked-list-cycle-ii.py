# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = set()
        
        while head:
            if head in hashmap:
                return head
            hashmap.add(head)
            head = head.next
            
        return None
        
        