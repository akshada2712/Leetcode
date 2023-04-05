class Solution:
    def tribonacci(self, n: int) -> int:
        
        k1,k2,k3 = 0,1,1
        
        while n > 0:
            k1,k2,k3 = k2,k3,k1+k2+k3
            n -= 1
            
        return k1