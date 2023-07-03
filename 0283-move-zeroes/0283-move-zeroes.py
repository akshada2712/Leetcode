class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0 and nums[l] == 0:
                nums[r], nums[l] = nums[l], nums[r]
            if nums[l] != 0:
                l += 1
        return nums