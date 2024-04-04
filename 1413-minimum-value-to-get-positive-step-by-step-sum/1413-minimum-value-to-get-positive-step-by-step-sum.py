class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        tot = 0 
        
        for num in nums:
            tot += num 
            print(tot)
            min_val = min(min_val, tot)
            
        return -min_val + 1
            
        