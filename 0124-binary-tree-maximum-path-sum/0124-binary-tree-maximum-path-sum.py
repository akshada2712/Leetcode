# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = -math.inf 
        
        def dfs(root):
            nonlocal max_sum
            if root is None:
                return 0 
            
            left_sum = max(dfs(root.left), 0)
            right_sum = max(dfs(root.right), 0)
            max_sum = max(max_sum, left_sum+right_sum + root.val )
            
            return max(left_sum + root.val, right_sum + root.val)
        
        dfs(root)
    
        return max_sum
            
        
        # dp = collections.defaultdict(list)
        # def dfs(node):
        #     if node.left is None and node.right is None:     # leaf node
        #         dp[node.val].append([node.val])
        #     if node.left:  
        #         dfs(node.left) 
        #     if node.right:
        #         dfs(node.right) 
        # dfs(root)
        # print(dp)
            
            
        