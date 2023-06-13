# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # first convert the tree into graph
        # then use normal bfs
        
        graph = defaultdict(list)
        
        def dfs(node):
#             nonlocal graph
            
#             if not node:
#                 return
            
#             if parent:
#                 graph[node].append(parent)
                
#             if node.left:
#                 create_graph(node.left, node)
                
#             if node.right:
#                 create_graph(node.right, node)

            if node:
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    dfs(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    dfs(node.right)     
                
        dfs(root)
        q = deque()
        q.append((target.val,0))
        
        visit = set()
        res = []
        while q:
            node, dist = q.popleft()
            visit.add(node)
            
            if dist == k:
                res.append(node)
                
            for nei in graph[node]:
                if nei not in visit:
                    q.append((nei, dist + 1))
                    
        return res
            
            
        
        