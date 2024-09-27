class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        counter_dct = Counter(nums)
        
        return counter_dct[target] > len(nums) / 2
        