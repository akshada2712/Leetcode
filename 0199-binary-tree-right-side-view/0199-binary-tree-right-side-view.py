# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = Queue()
        if not root:
            return []
        q.put(root)
        ans = []
        
        while q.qsize() > 0:
            n = q.qsize()
            for i in range(n):
                curr = q.get()
                if i == n - 1:
                    ans.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                    
                
        return ans
        