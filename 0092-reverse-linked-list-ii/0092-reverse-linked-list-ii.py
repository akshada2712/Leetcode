# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # solving this problem in three phase
        # creating pointers 
        
        dummy = ListNode(0, head)
        lprev, curr = dummy, head
        
        for i in range(left - 1):
            lprev, curr = curr, curr.next
            
        # lprev -> points to the node before left
        # curr -> point at the left node
        
        # reverse between left and right
        prev = None
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
            
        # update pointers
        lprev.next.next = curr
        lprev.next = prev
        
        return dummy.next
            
        