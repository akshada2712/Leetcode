"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        q = deque([(root, 1)])
        res = 0
        
        while q:
            node, depth = q.popleft()
            
            res = max(res, depth)
            
            if node.children:
                for child in node.children:
                    q.append((child, depth + 1))
                
        return res
        