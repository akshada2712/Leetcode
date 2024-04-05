class Solution:
    def trap(self, height: List[int]) -> int:
        
        # O(1) memory solution 
        
        if not height:
            return 0
       
        
        l = 0 
        r = len(height) - 1
        
        maxLeft = height[l] 
        maxRight = height[r]
        
        units = 0
        
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                units += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                units += maxRight - height[r]
                
                
        return units