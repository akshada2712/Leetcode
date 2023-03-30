class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # bottom up approach
        
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]   # take diagonal
                
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
                    
        return dp[0][0]
                    
        
        
        
        
#         text1_hash = {}
#         text2_hash = {}
                
#         for i in text1:
#             if i not in text1_hash:
#                 text1_hash[i] = 1
                
#             text1_hash[i] += 1
            
#         for i in text2:
#             if i not in text2_hash:
#                 text2_hash[i] = 1
                
#             text2_hash[i] += 1
            
#         cnt = 0
            
#         if len(text1_hash) >= len(text2_hash):
#             for i in text2_hash:
#                 if i in text1_hash and text1_hash[i] > 0:
#                     text1_hash[i] -= 1
#                     cnt += 1
                    
#         else:
#             for i in text1_hash:
#                 if i in text2_hash and text2_hash[i] > 0:
#                     text2_hash[i] -= 1
#                     cnt += 1
                    
#         return cnt
                    
            
        
            
            
        