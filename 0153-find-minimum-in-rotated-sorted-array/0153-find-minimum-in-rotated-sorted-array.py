class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        minVal = nums[0]  # keep track of minimum value 
        
        while low <= high and high < len(nums):
            
            if nums[low] < nums[high]:   # at a position where the minVal is found
                minVal = min(nums[low], minVal)
                break 
                
            
            mid = (low + high) // 2 
            minVal = min(nums[mid], minVal)
            
            if nums[mid] >= nums[low]:   # searching left
                low = mid + 1
                 
            else:  # searching right
                high = mid - 1 
                
        return minVal
            
            
        