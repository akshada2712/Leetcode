# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_two_sorted_lists(l1, l2):
            dummy = head = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val: 
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
        
        
        if not lists or len(lists) == 0:
            return None 
        ans = []
        while len(lists) > 1:
            ans = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                ans.append(merge_two_sorted_lists(l1, l2))
            lists = ans 
            
        return lists[0]