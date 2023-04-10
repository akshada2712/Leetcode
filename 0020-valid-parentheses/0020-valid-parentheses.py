class Solution:
    def isValid(self, s: str) -> bool:
        open_brack = ['{','(','[']
        close_brack = ['}',')',']']
        pairs = {'}':'{', ']':'[',')':'('}
        
        stack = []
        
        for i in s:
            if i in open_brack:
                stack.append(i)
            elif i in close_brack:
                if len(stack) == 0: return False 
                else: 
                    if stack[-1] == pairs[i]:
                        stack.pop()
                    else:
                        return False
                    
        if len(stack) == 0:
            return True
        else:
            return False