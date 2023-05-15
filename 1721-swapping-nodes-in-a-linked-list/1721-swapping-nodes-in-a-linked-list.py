# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        arr[k-1],arr[-k]=arr[-k],arr[k-1]
        print(arr)
        dummy = curr = ListNode(0)
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
            
        return dummy.next
            
        
        