# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        ## use bst property 
        
        
        curr = root
        
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
                
            else:
                return curr
        
#         def dfs(node):
#             if not node:
#                 return 
            
#             if (node.left == p and node.right == q) or (node.left == q and node.right == p):
#                 return node 
                
#             if (node == p and node.left == q) or (node == p and node.right == q) or (node == q and node.left == p) or (node == q and node.right == p):
                
#                 return node
                
                
#             dfs(node.left)
#             dfs(node.right)
            
#         return dfs(root)
            
             
        