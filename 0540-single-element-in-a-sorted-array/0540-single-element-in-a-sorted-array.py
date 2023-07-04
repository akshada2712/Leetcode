class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hash_ = Counter(nums)
        
        for i in hash_:
            if hash_[i] == 1:
                return i