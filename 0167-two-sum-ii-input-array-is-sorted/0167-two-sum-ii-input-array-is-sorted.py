class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l <= r:
            ans = numbers[l] + numbers[r]
            if ans > target:
                r -= 1
            elif ans < target:
                l += 1
            elif ans == target:
                return l+1, r+1
            
#         hashmap = {}
        
#         for i, val in enumerate(numbers):
#             ans = target - numbers[i]
#             if ans in hashmap:
#                 return [hashmap[ans] + 1,i+1] 
#             hashmap[val] = i
