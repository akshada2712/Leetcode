class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i,value in enumerate(nums):
            ans = target - nums[i]

            if ans in hash:
                return [i, hash[ans]]

            hash[value] = i
        # lst = sorted(nums)
        # l = 0
        # r = len(nums) - 1

        # while l < r:
        #     curr_sum = lst[l] + lst[r]

        #     if curr_sum == target:
        #         if lst[l] != lst[r]:
        #             return [nums.index(lst[l]),nums.index(lst[r])]
        #         else:
        #             return [nums.index(lst[l]),nums.index(lst[r])+1]

        #     elif curr_sum > target:
        #         r -= 1
        #     else:
        #         l += 1
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)-1):
        #         print(nums[i],nums[j],'nums[i],nums[j]')
        #         if nums[i] + nums[j] == target:
        #             return([i,j])
            # a = nums[i]
            # b = nums[i+1]
            # print(a,b)
            # if a + b == target:
            #     return ([i,i+1])