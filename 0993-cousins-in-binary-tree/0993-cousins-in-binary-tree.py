# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root,None, 0)])
        res = []
        
        while q:
            node, parent, ht = q.popleft()
            
            if len(res) == 2:
                break
                
            if node.val == x or node.val == y:
                res.append([parent, ht])
            
            if node.left:
                q.append((node.left,node, ht + 1))
                
            if node.right:
                q.append((node.right,node, ht + 1))
                
        n1, n2 = res
        
        return n1[0] != n2[0] and n1[1] == n2[1]
            
            
            
        