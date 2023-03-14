# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr, res):
            if not curr:
                return 0
            
            res =res * 10 + curr.val
            if not curr.left and not curr.right:
                return res
            return dfs(curr.left, res) + dfs(curr.right, res)
        
        return dfs(root, 0)