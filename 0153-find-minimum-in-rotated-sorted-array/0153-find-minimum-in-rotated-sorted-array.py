class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        minVal = nums[0]
        
        while low <= high and high < len(nums):
            
            if nums[low] < nums[high]:
                minVal = min(nums[low], minVal)
                break
                
            
            mid = (low + high) // 2 
            minVal = min(nums[mid], minVal)
            
            if nums[mid] >= nums[low]:
                low = mid + 1
                
            else:
                high = mid - 1 
                
        return minVal
            
            
        