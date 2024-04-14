# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        runnSum = 0
        
        def dfs(root, isLeft):
            nonlocal runnSum
            if not root:
                return 
            
            if not root.left and not root.right and isLeft:   # check leaf node 
                runnSum += root.val 
                
            dfs(root.left, True)
            dfs(root.right, False)
            
            
            return runnSum 
        
        return dfs(root, False)
                
        