# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = list1
        l2 = list2
        head = ListNode(0)
        dummy = head
        
        while l1 and l2: 
            val1 = l1.val 
            val2 = l2.val 
            
            if val1 <= val2:
                dummy.next = l1 
                l1 = l1.next 
            else:
                dummy.next = l2 
                l2 = l2.next 
            dummy = dummy.next 
            
            
        if l1:
            dummy.next = l1 
        
        if l2:
            dummy.next = l2 
            
        return head.next