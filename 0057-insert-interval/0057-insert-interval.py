class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        
        res = [intervals[0]]
        
        for start,end in intervals[1:]:
            prevEnd = res[-1][1]
            
            if start <= prevEnd:
                res[-1][1] = max(prevEnd, end)
            else:
                res.append([start,end])
                
        return res
                
        