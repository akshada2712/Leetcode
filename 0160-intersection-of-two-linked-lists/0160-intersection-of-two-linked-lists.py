# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        hash_ = set()

        while headA:
            if headA not in hash_:
                hash_.add(headA)

            headA = headA.next
        while headB:
            if headB in hash_:
                return headB
            headB = headB.next


#         l1, l2 = headA, headB

#         while l1 != l2:
#             l1 = l1.next if l1 else headB
#             l2 = l2.next if l2 else headA
#             print('l1',l1)
#             print('l2',l2)

#         return l1

        