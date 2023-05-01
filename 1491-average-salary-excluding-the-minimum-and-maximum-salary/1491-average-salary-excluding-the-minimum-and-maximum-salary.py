class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        currSum = 0
        for i in range(1,len(salary)-1):
            currSum += salary[i]
        
        return currSum / (len(salary)-2)