class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            graph[j].append(i)
             
        hashmap = {}   # map crs -> hashset of indirect prereqs
        
        def dfs(crs):
            if crs not in hashmap:
                hashmap[crs] = set()                
                for nei in graph[crs]:
                    hashmap[crs] |= dfs(nei)    # union of hashsets
                hashmap[crs].add(crs)
            return hashmap[crs]
                
        
        for crs in range(numCourses):
            dfs(crs)
        res = [] 
        for u,v in queries:
            res.append(u in hashmap[v])
        return res