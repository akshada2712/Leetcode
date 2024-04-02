class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        for i in s:
            if i == ')':
                rev_str = []
                
                while stack and stack[-1] != "(":
                    rev_str.append(stack.pop())
                    
                stack.pop()
                
                stack.extend(rev_str)
            else:
                stack.append(i)
                
        #print(stack)
        return "".join(stack)
                
#         open_brack = []
#         close_brack = []
#         s = list(s)
#         for idx, val in enumerate(s):
#             if val == "(":
#                 open_brack.append(idx)
#             elif val == ')':
#                 close_brack.append(idx)
                
#         open_brack.reverse()
        
#         def swap(x,y):
#             x, y = y, x
#             return 
        
#         for i, j in zip(open_brack, close_brack):
#             l = i + 1
#             r = j 
#             s.pop(i)
#             s.pop(j-1)
#             print(l,r)
#             while l < r and l < len(s) and r <= len(s):
#                 print(l,r)
#                 s[l], s[r] = s[r], s[l]
#                 print(s)
#                 l += 1
#                 r -= 1
            #print(s)
            
#         stack = []
        
#         for i in s:
#             if i == ")":
#                 for idx, val in enumerate(stack[::-1s]):
#                     if val == "(":
                        
                    
                
                
        