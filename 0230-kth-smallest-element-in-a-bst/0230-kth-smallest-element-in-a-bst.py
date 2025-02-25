# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        trav = []
        
        def dfs(root):
            
            if len(trav) == k:
                return trav[-1]
            
            if not root:
                return 
        
            
            if root.left:
                dfs(root.left)
                
            trav.append(root.val)
            
            
            if root.right:
                dfs(root.right)
            #print(len(trav))
            
        dfs(root)
        
        
        return trav[k-1]
        