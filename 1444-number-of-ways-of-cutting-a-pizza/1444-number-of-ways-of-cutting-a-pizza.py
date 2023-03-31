class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        @cache
        def has_apple(start_r, start_c, end_r, end_c):
            for r in range(start_r, end_r + 1):
                for c in range(start_c, end_c+1):
                    if pizza[r][c] == "A":
                        return True
                    
            return False
        
        @cache
        def dp(start_r, start_c, slices_left):
            
            if slices_left == 1:
                if has_apple(start_r, start_c, len(pizza)-1, len(pizza[0]) -1 ):
                    return 1
                
            num_ways = 0
            for i in range(start_c+1, len(pizza[0])):
                if has_apple(start_r, start_c, len(pizza)-1, i-1):
                    num_ways += dp(start_r, i, slices_left-1)
                    
            for j in range(start_r+1, len(pizza)):
                if has_apple(start_r, start_c, j-1, len(pizza[0])-1):
                    num_ways += dp(j, start_c, slices_left -1)
            return num_ways
        
        return dp(0,0,k) % (10 ** 9 + 7)
        