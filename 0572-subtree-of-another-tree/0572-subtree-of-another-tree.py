# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def sameTree(self, s, p):
        if not s and not p:
            return True
        if s and p and s.val == p.val:
            return self.sameTree(s.left, p.left) and self.sameTree(s.right, p.right)
        
        return False
            
        
        
#         def dfs(root, subRoot):
#             if root is None:
#                 return True
#             if subRoot is None:
#                 return
#             if root.val == subRoot.val:
#                 return True
#             return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
        
#         return dfs(root, subRoot)
        