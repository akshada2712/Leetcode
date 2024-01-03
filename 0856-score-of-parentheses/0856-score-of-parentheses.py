class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]   # let initial score be 0 
        
        for i in s:
            if i == '(':
                stack.append(0)
            elif i == ')':
                score = stack.pop()
                stack[-1] += max(2*score, 1)
                    
        return stack[-1]
                
        