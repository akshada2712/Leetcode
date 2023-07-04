class Solution:
    def arrangeCoins(self, n: int) -> int:
        m = n
        if n == 1 or n == 2:
            return 1
        for i in range(n):
            m = m - i
            if m == 0:
                return i 
            elif m < 0:
                return i - 1
            
            
        