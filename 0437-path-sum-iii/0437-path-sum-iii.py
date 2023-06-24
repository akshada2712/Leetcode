# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        cnt = 0
        prefix_sum = {0:1}
        
        def dfs(root, currSum):
            nonlocal cnt
            if not root:
                return
            
            currSum += root.val
            cnt += prefix_sum.get(currSum - targetSum,0)
            prefix_sum[currSum] = prefix_sum.get(currSum,0)+1
            
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            
            prefix_sum[currSum] -= 1
            
        dfs(root, 0)
        return cnt
            
            
            
        