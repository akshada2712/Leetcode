class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+','-','/','*'}
        stack = []
        
        for i in tokens:
            if i in op:
                x = stack.pop(-1)
                y = stack.pop(-1)
                if i == '+':
                    stack.append(x+y)
                elif i == '-':
                    stack.append(y-x)
                elif i == '*':
                    stack.append(x*y)
                elif i == '/':
                    stack.append(int(y/x))
                    
            else:
                stack.append(int(i))
                
        return stack[-1]
        