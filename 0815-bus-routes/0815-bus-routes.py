class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if target == source:
            return 0
        
        adjGraph = defaultdict(set)
        
        for grp, route in enumerate(routes):
            for stop in route:
                adjGraph[stop].add(grp)
                
        # print(adjGraph)  {1: {0}, 2: {0}, 7: {0, 1}, 3: {1}, 6: {1}})
        
        q = [(source, 0)]
        visited = set()
        
        for stop, buses in q:
            if stop == target:
                return buses 
            
            for grp in adjGraph[stop]:
                for nei in routes[grp]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, buses + 1))
                        
                routes[grp] = []
                
        return -1
        
#         busMap = {i+1:routes[i] for i in range(len(routes))}
        
#         q = []
#         tot = 0
#         q.append(source)
#         while q:
#             currNode = q.pop(-1)
#             for i in busMap:
                
#                 if currNode in busMap[i]:
#                     tot += 1
#                     vals = busMap.get(i)
#                     q.append(k for k in vals)
#                 print(q)
#         return -1