# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def helper(root,path):
            if root is None:
                return
            if root.left is None and root.right is None:
                path.append(str(root.val))
                ans.append("->".join(path))
                path.pop()
                return
            
            path.append(str(root.val))
            helper(root.left,path)
            helper(root.right,path)
            path.pop()
            
        helper(root,[])
        return ans