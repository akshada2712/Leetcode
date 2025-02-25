# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # 2nd method 
        
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
        
        # 1st method
#         values = []
        
        
#         def dfs(node):
#             if not node:
#                 return 
            
#             dfs(node.left)
#             values.append(node.val)
#             dfs(node.right)
        
#         dfs(root)
        
#         ans = 0
#         for i in range(len(values)):
#             if values[i] == low:
#                 while values[i] != high: 
#                     ans += values[i]
#                     i += 1
                    
#                 ans += high 
                
#                 break 
                
#         return ans
            