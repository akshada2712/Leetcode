class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total , current = 0, 0
        
        for i in nums:
            if i == 0:
                current += 1
                total += current
            else:
                current = 0
                
        return total
        