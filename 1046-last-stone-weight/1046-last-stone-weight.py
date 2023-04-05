class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = stones
        
        while len(nums) > 1:
            largest = heapq.nlargest(2, nums)
            #print(largest)
            x = largest[0]
            y = largest[1]
            
            if x == y:
                nums.pop(nums.index(x))
                nums.pop(nums.index(y))
            else:
                nums.pop(nums.index(x))
                idx = nums.index(y)
                nums[idx] = abs(y - x)
                
        return nums[0] if nums else 0
        