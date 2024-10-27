"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # using two ptr approach 
        # Approach 1: find all ancestors for both p and q an =d then find the common one 
        # aproach 2: traverse the parent nodes and check at any point both pointers become eqauk 
        
        ptr1, ptr2 = p, q 
        
        while ptr1 != ptr2:
            ptr1 = ptr1.parent if ptr1 else q 
            
            ptr2 = ptr2.parent if ptr2 else p 
            
        return ptr1
            