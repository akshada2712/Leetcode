# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def findleaf(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [node.val]
            
            return findleaf(node.left) + findleaf(node.right)
        
        return findleaf(root1) == findleaf(root2)
        
        
#         lst1 = []
#         lst2 = []
        
        
#         def dfs(root1, root2):
#             nonlocal lst1
#             nonlocal lst2
#             if not root1 or not root2:
#                 return
            
#             if not root1.left and not root1.right :
#                 lst1.append(root1.val)
#                 return
                
#             if not root2.left and not root2.right:
#                 lst2.append(root2.val)
#                 return
                
#             if root1.left:
#                 dfs(root1.left, root2.left)
            
#             if root1.right:
#                 dfs(root1.right, root2.right)
                
#         dfs(root1, root2)
        
#         print(lst1, lst2)
                
        
        