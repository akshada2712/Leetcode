# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, path, currSum):
            if not root:
                return 
            currSum += root.val
            path.append(root.val)
            
            if not root.left and not root.right and currSum == targetSum:
                res.append(path)
                
                
            dfs(root.left,list(path),currSum)
            dfs(root.right,list(path),currSum)
            
        
        dfs(root,[],0)
        return res
                
            
            
            
        