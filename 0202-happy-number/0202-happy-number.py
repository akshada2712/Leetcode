class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()
        
        def get_nextn(n):
            tot_sum = 0
            while n > 0:
                n , digit = divmod(n, 10)
                tot_sum += digit ** 2 
                
            return tot_sum
        
        while n != 1 and n not in visit:
            visit.add(n)
            n = get_nextn(n)
            
        return n == 1
            