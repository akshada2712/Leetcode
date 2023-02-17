#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        temp1 = l1
        temp2 = l2
        carry = 0
        
        while temp1 is not None or temp2 is not None or carry != 0:
            val1 = temp1.val if temp1 is not None else 0
            val2 = temp2.val if temp2 is not None else 0
            
            valSum = val1 + val2 + carry
            
            nodeVal = valSum % 10
                        
            newNode = ListNode(nodeVal)
            curr.next = newNode
            curr = newNode
            
            carry = valSum // 10
            
            temp1 = temp1.next if temp1 is not None else None
            temp2 = temp2.next if temp2 is not None else None
            
        return dummy.next