class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0 
        
        left, right = 0, len(height) - 1
        lMax, rMax = 0, 0
        
        trapped_water = 0
        
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= lMax:
                    lMax = height[left]
                else:
                    trapped_water += lMax - height[left]
                    
                left += 1
                
            else:
                if height[right] >= rMax:
                    rMax = height[right]
                else:
                    trapped_water += rMax - height[right]
                    
                right -= 1 
                
        return trapped_water