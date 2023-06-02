# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        currSum = 0
        
        def dfs(node):
            nonlocal currSum
            if not node:
                return 0
            
            if node.val >= low and node.val <= high:
                currSum += node.val
                
            dfs(node.left)
            dfs(node.right)
            
            return currSum
            
        return dfs(root)
        