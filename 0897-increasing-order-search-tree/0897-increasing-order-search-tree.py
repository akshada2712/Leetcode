# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.head = TreeNode(0)
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            
            self.head.right = TreeNode(node.val)
            self.head = self.head.right
            dfs(node.right)
            
            
        dfs(root)
        return ans.right
        