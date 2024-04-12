class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        
        stack = []
        
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -=1
         
            stack.append(i)
            
        res = stack[:-k] if k else stack
        
        
                 
        return "".join(res).lstrip('0') or "0"
        