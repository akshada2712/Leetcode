class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        
        q = deque([0])
        
        while q:
            curr = q.popleft()
            visit.add(curr)
            
            for i in rooms[curr]:
                if i not in visit:
                    q.append(i)
                    
        return len(visit) == len(rooms)
                    