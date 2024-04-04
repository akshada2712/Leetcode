class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        tot = 0 
        pref_sum = [0] * len(nums)
        pref_sum[0] = 0
        
        for num in nums:
            pref_sum.append(pref_sum[-1] + num)
            # tot += num 
            # print(tot)
            # min_val = min(min_val, tot)
            
        return -min(pref_sum) + 1
            
        