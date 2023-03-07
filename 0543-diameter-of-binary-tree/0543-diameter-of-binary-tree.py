# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            return 1 + max(dfs(root.left),dfs(root.right)) if root else 0
        if root is None: return 0
        d1 = dfs(root.left) + dfs(root.right)
        d2 = self.diameterOfBinaryTree(root.left)
        d3 = self.diameterOfBinaryTree(root.right)
        
        
        return max(d1,max(d2,d3))