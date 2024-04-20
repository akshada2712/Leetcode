import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = []
        heapq.heapify(res)
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:x[0])
        heapq.heappush(res, intervals[0][1])
        
        for i in intervals[1:]:
            if res[0] <= i[0]:
                heapq.heappop(res)
                
            heapq.heappush(res, i[1])
            
        return len(res)
        
#         for i in range(len(intervals)):
#             if res and res[-1][1] <= intervals[i][0]:
#                 res.pop(-1)
#             res.append(intervals[i])
        
#         return len(res)
                    
                
            