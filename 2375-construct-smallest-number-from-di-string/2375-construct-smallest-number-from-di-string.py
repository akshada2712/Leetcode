class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        n = len(pattern)
        ans = [i for i in range(1, n + 2)]
        
        for i in range(1, n + 1):
            if pattern[i - 1] == ' I' and ans[i - 1] > ans[i] or pattern[i-1] == "D" and ans[i-1] < ans[i]:
                start = end = i - 1
                while end < n and pattern[end] == "D": 
                    end += 1
                    
                ans[start:end+1] = ans[start:end + 1][::-1]
                
        return "".join(str(i) for i in ans)
        
        
#         arr = [i for i in range(1, len(pattern) + 2)]
#         #print(arr)
#         l = 0
#         r = 1
#         n = len(pattern)
        
#         def swap(l,r):
#             while l <= r:
#                 arr[l], arr[r] = arr[r], arr[l]
#                 l += 1
#                 r -= 1
        
#         while l < r and r < n:
            
#             if arr[l] < arr[r]:
#                 if pattern[l] == 'I':
#                     l += 1
#                     r += 1
#                 elif pattern[l] == 'D':
                    
#                     while r < n and pattern[r] == 'D' and r <= n:
#                         #print(r)
#                         r += 1
                        
#                     # print(arr)
#                     # print(l, r)
#                     #arr[l-1:r+1] = arr[r:l:-1]
                    
#                     #swap(l,r)
#                     arr[l:r + 1] = arr[l:r + 1][::-1]
#                     l = r
#                     r += 1
#                     #print(l,r)
                    
                    
#         return ''.join(str(i) for i in arr)
#             #print(l,r)
#             if pattern[l] == "I":
#                 if arr[l] < arr[r]:
#                     l += 1
#                     r += 1
#             elif pattern [l] == "D":
#                 if arr[r] > arr[l]:
#                     arr[l], arr[r] = arr[r], arr[l]
#                     l += 1
#                     r += 1
        
#         return "".join(str(i) for i in arr)