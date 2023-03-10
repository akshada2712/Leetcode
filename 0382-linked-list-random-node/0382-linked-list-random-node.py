# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        curr = self.head
        rand_var = 0
        curr_len = 1
        while curr:
            if random.random() < (1 / curr_len):
                rand_var = curr.val
            curr_len += 1
            curr = curr.next
            
        return rand_var
            
            
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()