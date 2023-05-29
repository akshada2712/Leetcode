class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        q.append(start)
        n = len(arr)
        visit = set()
        
        while q:
            curr = q.popleft()
            
            if curr in visit:
                continue
            else:
                visit.add(curr)
            
            if curr < 0 or curr >= len(arr):
                continue
            
            val = arr[curr] 
            if val == 0:
                return True
            q.append(curr + val)
            q.append(curr - val)
                
        
        return False
            