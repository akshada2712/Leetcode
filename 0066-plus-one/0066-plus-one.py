class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        dig = int(''.join(digits))
        dig = str(dig + 1)
        ans = [int(s) for s in dig]
        return ans
        
        