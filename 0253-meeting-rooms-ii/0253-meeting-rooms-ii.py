class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key= lambda x:x[0])
        minHeap = []
        
        heapq.heappush(minHeap, intervals[0][1])
        
        for i in intervals[1:]:
            if minHeap[0] <= i[0]:
                heapq.heappop(minHeap)
                
            heapq.heappush(minHeap, i[1])
            
        return len(minHeap)
        