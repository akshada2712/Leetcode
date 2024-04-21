# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, low, high):
            if not node:
                return True 
            
            if not (node.val > low and node.val < high):
                return False
            
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)
        
        
        return valid(root, -math.inf, math.inf)
            
        
#         def dfs(node):
#             if not node.left and not node.right:
#                 return 
            
#             if node.left.val < node.val and node.val < node.right.val:
#                 return dfs(node.left) and dfs(node.right)
            
#         return dfs(root)