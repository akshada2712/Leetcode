class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        # dynamic programming - matrix solution
        
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1)+1)]
        
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[len(nums1)][len(nums2)]
        
#         # recursive memoization solution
        
#         def helper(i,j):
#             if i == len(nums1) or j == len(nums2):
#                 return 0
            
#             if (i,j) in dp:
#                 return dp[(i,j)]
            
#             if nums1[i] == nums2[j]:
#                 dp[(i,j)] = 1 + helper(i+1, j+1)
                
#             else:
#                 dp[(i,j)] = max(helper(i+1,j), helper(i,j+1))
#             return dp[(i,j)]
        
#         dp = {}
#         return helper(0,0)
        
        
#         hash1 = {}
#         hash2 = {}
        
#         for i in range(len(nums1)):
#             hash1[nums1[i]] = i
            
#         for i in range(len(nums2)):
#             hash2[nums2[i]] = i
            
            
#         cnt = set()
#         cnt.add(0)
        
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i] == nums2[j] and j > max(cnt):
#                     cnt.add(j)
                    
#         return 0 if len(cnt) == 1 else len(cnt)
            
            
        