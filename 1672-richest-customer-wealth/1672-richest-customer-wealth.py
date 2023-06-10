class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        curr_max = float('-inf')
        
        for i in accounts:
            curr_max = max(curr_max, sum(i))
            
        return curr_max
        