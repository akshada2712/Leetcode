class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        hashmap = {}
        n = len(nums)
        
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for i in hashmap:
            if hashmap[i] > math.floor(n/3):
                res.append(i)
                
        return res
        