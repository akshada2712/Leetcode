# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node): 
            if node is None:
                return False 
            
            elif sameTree(node, subRoot):
                return True 
            
            return dfs(node.left) or dfs(node.right)
            
        def sameTree(p,q):
            if p is None or q is None:
                return p is None and q is None
            
            return (p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right))
        
        
        return dfs(root)
        