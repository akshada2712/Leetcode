class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        # add first room to the queue
        q = deque([0])
        # we will chk the length of visit room == len(rooms)
        while q:
            curr = q.popleft()
            visit.add(curr)
            
            for i in rooms[curr]:
                if i not in visit:
                    q.append(i)
                    
        return len(visit) == len(rooms)
                    