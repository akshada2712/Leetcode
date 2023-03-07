# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        hashmap = defaultdict(list)
        q = collections.deque([(root, 0, 0)])
        
        res = []
        #print(q.get())
        while q:
            n = len(q)
            for _ in range(n):
                node, x, y = q.popleft()
                #print(node,x,y)
                hashmap[x].append((y,node.val)) 
                if node.left:
                    q.append((node.left,x-1,y+1))                
                if node.right:
                    q.append((node.right,x+1,y+1))
                    
            #break
                
                
        for level in sorted(hashmap.keys()):
            res.append(tup[1] for tup in sorted(hashmap[level]))
            
            
        return res
                
                
        
        
        
        