class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()  # first sort 
        # loop through to check overlaps 
        for i in range(len(intervals) - 1):
            # compare the second element with the first element of next interval eg : 
            # [0,30], [5,10] -> 30 >  5 -> False 
            # [2,4], [7, 10] -> 4 is not > 7 and list ends hence True
            
            if intervals[i][1] > intervals[i+1][0]:
                return False 
            
        return True
        