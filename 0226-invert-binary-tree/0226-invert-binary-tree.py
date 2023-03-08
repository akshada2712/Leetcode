# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def swap(tree):
            tree.left, tree.right = tree.right, tree.left
            
        q = [root]
        
        while q:
            curr = q.pop()
            if curr is None:
                continue
            swap(curr)
            q.append(curr.left)
            q.append(curr.right)
            
        return root
        