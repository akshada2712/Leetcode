class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        i = ans = 0
         
        
        n = len(arr)
        if n < 3:
            return 0
        
        while i < n:
            base = i 
            
            while i + 1 < n and arr[i] < arr[i+1]:
                i += 1
            # once we exit from above loop we have acheieved a point where its peak
            peak = i 
            
            # above loop didnt execute
            if i == base:
                i += 1
                
                continue 
            # now we have to check for lesser points or where the value increases again
            while i + 1 < n and arr[i] > arr[i+1]:
                i += 1
                
            if i == peak:        #if above loop didnt execute
                i += 1
                continue
                
            ans = max(ans, i - base + 1)
            
        return ans
        
#         l = 0
#         r = 2 
#         mtnLen = 0
        
#         while l < r and r < len(arr) - 1:
#             m = (l + r) // 2
#             #print(l,r)
            
#             if arr[m] > arr[l] and arr[m] > arr[r]:
#                 mtnLen = max(mtnLen, r - l + 1)
#                 r += 1
#             elif arr[l] < arr[m] and arr[r] > arr[m]:
#                 r += 1
#             elif arr[m] < arr[l] and arr[m] < arr[r]:
#                 r += 1
#                 l += 1
                
#         return mtnLen
            
                
        
        
         
            
        
#         minLefts = [0] * len(arr)
#         minRights = [0] * len(arr)
#         n = len(arr)
#         l = 0
#         r = n - 1
#         minLval = arr[l]
#         minRval = arr[r]
#         minLefts[0] = arr[l]
#         minRights[n - 1] = arr[n - 1]
#         print(minRights)
#         ans = [0] * len(arr)
#         for i in range(1, n):
#             #minLVal = min(minLVal, arr[i])
            
#             minLefts[i] = min(arr[i], minLefts[i - 1])
            
#         for i in range(n - 2, -1, -1):
#             #print(arr[i], )
#             minRights[i] = min(arr[i], minRights[i + 1])
            
#         for i, j in zip(minLefts, minRights):
#             idx = 0
#             val = j - i
           
#             if idx >= n:
#                 break
#             ans[idx] = val if val > 0 else 0
#             idx += 1
            
#         return sum(ans) + 1
            
            
        