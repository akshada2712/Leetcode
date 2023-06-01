# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        val = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            val.append(node.val)            
            dfs(node.right)
        dfs(root)    
        res = float('inf')
        for i in range(len(val)-1):
            res = min(res, abs(val[i+1] - val[i]))
        return res