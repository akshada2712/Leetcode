class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[0])
        if not intervals:
            return True
        for i in range(len(intervals)+1):
            if i == len(intervals) - 1:
                return True
            inter = intervals[i]
            inter2 = intervals[i+1]
            if inter2[0] - inter[1] < 0:
                return False
            
        return True