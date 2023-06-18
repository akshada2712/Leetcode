class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # we will use Kahn's Algo -> as there is dependencies
        
        graph = defaultdict(list)
        
        for i, j in prerequisites:
            graph[j].append(i)
            
        in_deg = [0] * numCourses
        
        for i in range(numCourses):
            for j in graph[i]:
                in_deg[j] = in_deg[j] + 1
                
        # print(in_deg, graph)
        
        q = deque()   # queue to hold course with 0 prereq
        
        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)
            
        idx = 0
        order = [0] * numCourses
        
        while q:
            node = q.popleft()
            
            order[idx] = node
            idx += 1
            for nei in graph[node]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    q.append(nei)
                    
        return order if idx == numCourses else []
            
            
            
        