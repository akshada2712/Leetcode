class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        for i in s:
            if i == ')':
                rev_str = []   # create a array to capture reverse strings
                
                while stack and stack[-1] != "(":
                    rev_str.append(stack.pop())   # till we encounter open brack we would be adding the element by popping frm stack
                    
                stack.pop()   # popping the open brack
                 
                stack.extend(rev_str)   # adding the reversed element to the last of list
            else:
                stack.append(i)    # if its just char
                
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
                        
                    
                
                
        