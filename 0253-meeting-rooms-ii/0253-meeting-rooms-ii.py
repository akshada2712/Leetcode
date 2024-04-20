import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
         # approach 2 - using two pointers Time - O(nlogn)  Space - O(n)
            
        start = [x[0] for x in intervals]
        end = [x[1] for x in intervals]
        
        start.sort()
        end.sort()
        
        count = 0
        
        l = 0 
        r = 0
        res = 0
        
        while l < len(start):
            print(l, r)
            if start[l] < end[r]:
                
                count += 1
                print(count)
                l += 1
            else:
                r += 1
                count -= 1
            res = max(res, count)  
        #print(count)
        return res
        
        # approach 1 - heapq
#         res = []
#         heapq.heapify(res)
#         if not intervals:
#             return 0
        
#         intervals.sort(key = lambda x:x[0])
#         heapq.heappush(res, intervals[0][1])
        
#         for i in intervals[1:]:
#             if res[0] <= i[0]:
#                 heapq.heappop(res)
                
#             heapq.heappush(res, i[1])
            
#         return len(res)
        
                    
                
            