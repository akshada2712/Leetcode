class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, val in enumerate(numbers):
            ans = target - numbers[i]
            if ans in hashmap:
                return [hashmap[ans] + 1,i+1] 
            hashmap[val] = i