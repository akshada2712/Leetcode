class Solution:
    def calculate(self, s: str) -> int:
        
        def evaluate(x, y, op):
            if op == "+":
                return x
            if op == '-':
                return -x 
            if op == '*':
                return x * y 
            
            return int(x/y)
        
        s += '@'
        stack = []
        curr = 0
        prevOp = "+"
        
        
        for c in s:
            if c.isdigit():
                curr = curr * 10 + int(c)
                
            elif c == '(':
                stack.append(prevOp)
                prevOp ="+"
                
            else:
                if prevOp in "*/":
                    stack.append(evaluate(stack.pop(), curr, prevOp))
                else:
                    stack.append(evaluate(curr, 0, prevOp))
                
                curr = 0
                prevOp = c
                if c == ')':
                    while type(stack[-1]) == int:
                        curr += stack.pop()
                    prevOp = stack.pop()
                    
        return sum(stack)
    
    
    
    
#         stack = []
#         curr = 0
#         prevOp = "+"
#         s += "@"
        
#         for i in s:
#             print(stack,i,prevOp)
#             if i.isdigit():
#                 curr = curr * 10 + int(i)
#             elif i == '(':
#                 stack.append(prevOp)
#                 prevOp = "+"
#             else:
#                 if prevOp == "+":
#                     stack.append(curr)
#                 elif prevOp == '-':
#                     stack.append(-curr)
#                 elif prevOp == '*':
#                     stack.append(stack.pop() * curr)
#                 elif prevOp == '/':
#                     stack.append(math.trunc(stack.pop() / curr))
#                 curr = 0
#                 prevOp = i 
#                 if i == ')':
#                     while type(stack[-1]) == int():
#                         curr += stack.pop()
#                     prevOp = stack.pop()
#         print(stack)           
#         return sum(stack)
        