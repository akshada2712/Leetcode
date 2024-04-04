class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # top down approach -> gives TLE
        
#         points = defaultdict(int)
#         max_num = 0
        
#         for num in nums:
#             points[num] += num
#             max_num = max(max_num, num)
            
#         def return_max(num):
#             if num == 0:
#                 return 0
#             if num == 1:
#                 return points[1]
            
#             return max(return_max(num - 1), return_max(num - 2) + points[num])
        
#         return return_max(max_num)
        
        
        #bottom up approach
        points = defaultdict(int)
        max_num = 0
        
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)
            
        dp = [0] * (max_num + 1)
        dp[1] = points[1]
        
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])
            
        return dp[max_num]
            
            
#         cntr = Counter(nums)
#         #nums = list(set(nums))
#         nums.sort()
#         print(nums)
#         print(cntr)
#         dp = [0] * len(nums)
#         dp[1] = cntr[nums[1]]
        
        
#         for i in range(2,len(nums)):
#             if nums[i] == nums[i-1] + 1:
#                 dp[i] = max(cntr[nums[i]] * nums[i] + dp[i - 2], dp[i - 1]) 
# #             else:
# #                 dp[i] = dp[i -  1] + cntr[nums[i]] * nums[i]
        
#         print(dp)
#         return dp[-1]
        
#         hash = Counter(nums)
#         nums = list(set(nums))
#         nums.sort()
        
#         e1, e2 = 0, 0
#         for i in range(len(nums)):
#             currEarn = nums[i] * hash[nums[i]]
            
#             if nums[i] + 1 == nums[i+1]:
#                 e1
            
      
        #print(hash, nums)
#         dp = [0] * len(nums)
#         #print(len(dp))
#         #print(nums[0], hash[nums[0]])
#         dp[0] = nums[0] * hash[nums[0]]
#         for i in range(1, len(nums)):
#             if nums[i - 1] + 1 == nums[i]:
#                 print(dp)
#                 dp[i] = max(dp[i-1], nums[i] * hash[nums[i]])
#             else:
#                 print(dp)
#                 dp[i] = dp[i - 1] + nums[i] * hash[nums[i]]
                
#         print(dp)