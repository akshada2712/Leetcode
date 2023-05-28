# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dp = {}
        
        def dfs(node):
            if not node:
                return
            if node.val in dp:
                dp[node.val] += 1
            else:
                dp[node.val] = 1
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        lst = []
        for i in dp:
            if dp[i] == max(dp.values()):
                lst.append(i)
        return lst if len(lst) >= 1 else [0]
    
        