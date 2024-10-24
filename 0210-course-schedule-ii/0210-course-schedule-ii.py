class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses 
        q = deque()
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        ans = []
        
        while q:
            node = q.popleft()
            
            ans.append(node)
            
            for nei in graph[node]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    q.append(nei)
                    
        return ans if len(ans) == numCourses else []
        