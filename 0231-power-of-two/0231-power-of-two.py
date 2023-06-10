class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: 
            return False
        if n == 1 or n == 2:
            return True
        
        if n == 3:
            return False
        
        while n >= 3:
            if n % 2 != 0:
                return False
            else:
                n = n // 2
                
        return True
                
                
        