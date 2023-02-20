# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # array solution
        string = []
        
        while head:
            string.append(head.val)
            head = head.next
            
        return string == string [::-1]
        