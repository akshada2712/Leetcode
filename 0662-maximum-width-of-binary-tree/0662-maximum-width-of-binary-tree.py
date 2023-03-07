# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,1)])        
        width = 0        
        while q:
            _, left = q[0]
            _, right = q[-1]
            width = max(width, right-left+1)
            next_level = deque()            
            while q:
                node, idx = q.popleft()
                if node.left:
                    next_level.append((node.left,2*idx))
                if node.right:
                    next_level.append((node.right, 2*idx+1))                    
            q = next_level         
        return width