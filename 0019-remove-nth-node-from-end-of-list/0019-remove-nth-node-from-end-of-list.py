# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next 
            n -= 1
            
        while right:
            left = left.next
            right = right.next 
            
        left.next = left.next.next
        
        return dummy.next
        
#         length = 0
        
#         while dummy:
#             dummy = dummy.next 
#             length += 1
            
#         #print(length)
        
#         offset = length - n
#         slow = head
#         fast = head.next
#         for i in range(offset - 1):
#             slow = slow.next
#             fast = fast.next 
            
#         if fast:
#             slow.next = fast.next 
#             fast.next = None
        
#         return head
        
        
            
#         print(slow, fast)
            
            
        