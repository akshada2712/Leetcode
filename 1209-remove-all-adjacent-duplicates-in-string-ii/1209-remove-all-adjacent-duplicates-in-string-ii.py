class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append([i,1])
            else:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop(-1)
        string = ""       
        for i,j in stack:
            string += i * j
        return string
            
        
#         dct = collections.OrderedDict()
        
#         for i in s:
#             if i in dct:
#                 dct[i] += 1
#             else:
#                 dct[i] = 1
                
#             if dct[i] == k:
#                 dct.pop(i)
                
#         string =""       
#         for i in dct:
#             if dct[i]:
#                 string += dct[i] * i
                
#         return string
            
#         stack = [s[0]]
#         for i in range(1, len(s)):
#             stack.append(s[i])
#             if stack[-1] == s[i]:
#                 if stack:
#                     for i in range(k):
#                         stack.pop(-1)
# #             while len(stack) >= 1 and stack[-1] == s[i]:
# #                 for i in range(k):
# #                     stack.pop(-1)
                    
#         print(s)
                
        