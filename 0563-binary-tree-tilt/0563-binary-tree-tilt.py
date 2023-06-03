# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        totTilt = 0
        
        def dfs(node):
            nonlocal totTilt
            if node is None:
                return 0
            if not node.left and not node.right:
                return node.val
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            
            totTilt += abs(leftSum - rightSum)
            
            return leftSum + rightSum + node.val
        
        dfs(root)
        
        return totTilt
            
        