# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        values = []
        while head:
            values.append(head.val)
            head = head.next
            
        def helper(start,end):
            if start > end:
                return
            mid = (start + end)// 2
            node = TreeNode(values[mid])
            node.left = helper(start,mid-1)
            node.right = helper(mid+1,end)
            
            return node
        
        return helper(0,len(values)-1)
        