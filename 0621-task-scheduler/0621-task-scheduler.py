class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # we will use max heap to store counters
        # and a queue to check at what time the task would be available 
        # (counter, time + n)
        cnt = Counter(tasks)
        maxHeap = [-count for count in cnt.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        
        while q or maxHeap:
            time += 1 
            
            if maxHeap: 
                cnt = 1 + heapq.heappop(maxHeap)
                
                if cnt: 
                    q.append((cnt, time + n))   # at this the task would be available 
                    
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time
        