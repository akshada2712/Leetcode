class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visit = set()  # (src,dst)
        ans = []
        
        def dfs(node,path,ans):
            
            if node == len(graph)-1:
                ans.append(path)
            
            for i in graph[node]:
                dfs(i,path+[i],ans)
                
        dfs(0,[0],ans)
        return ans