# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = {}
        
        def bfs(root,level=0):
            if not root: return
            
            if level not in hashmap:
                hashmap[level] = [root.val]
            else:
                hashmap[level].append(root.val)
                
            bfs(root.left,level+1)
            bfs(root.right,level+1)
            
            
        bfs(root)
        
        ans = []
        for i in hashmap:
            ans.append(hashmap[i])
            
            
        return ans
        