class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        wld_stack = []
        
        for i in range(len(s)):
            #print(i,stack,wld_stack)
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                wld_stack.append(i)
                
            elif s[i] == ')':
                if stack:
                    stack.pop()
                elif wld_stack:
                    wld_stack.pop()
                else:
                    return False
                
        while stack and wld_stack:
            if stack[-1] > wld_stack[-1]:
                return False
            stack.pop()
            wld_stack.pop()
            
        return len(stack) == 0
            
        
        
                    
        