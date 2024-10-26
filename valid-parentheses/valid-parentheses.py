class Solution:
    def isValid(self, s: str) -> bool:
        open_brack = {'(', '{', '['}
        brack_set = {'{': '}', '[':']', '(':')'}
        close_brack = {'}',')', ']'}
        stack = []
        for i in s:
            if i in open_brack:
                stack.append(i)
            else:
                if stack:
                    if brack_set[stack[-1]] == i:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False 
                    
        if len(stack) == 0:
            return True 
        else:
            return False
            
        