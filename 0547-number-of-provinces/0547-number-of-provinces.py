class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        
        def dfs(node):
            if node in seen:
                return 0
            
            seen.add(node)
            
            for i in range(len(isConnected[node])):
                if isConnected[node][i]:
                    dfs(i)
            return 1
                    
        pro = 0       
        for i in range(len(isConnected)):
            if i not in seen:
                pro += dfs(i)
            
        return pro
        