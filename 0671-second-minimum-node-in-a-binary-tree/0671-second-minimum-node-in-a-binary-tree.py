# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        hashmap = set()
        
        def dfs(node):
            if not node:
                return
            if node in hashmap:
                return
            hashmap.add(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        lst = list(hashmap)
        lst.sort()
        return lst[1] if len(lst) >= 2 else -1
        