# class Solution:
#     def calculate(self, s: str) -> int:
        
#         def evaluate(x, y, op):
#             if op == "+":
#                 return x
#             if op == '-':
#                 return -x 
#             if op == '*':
#                 return x * y 
#             return math.trunc(x/y)
#         s += '@'
#         stack = []
#         curr = 0
#         prevOp = "+"
        
        
#         for c in s:
#             if c.isdigit():
#                 curr = curr * 10 + int(c)
                
#             elif c == '(':
#                 stack.append(prevOp)
#                 prevOp ="+"
                
#             else:
#                 if c in "*/":
#                     stack.append(evaluate(stack.pop(), curr, prevOp))
#                 else:
#                     stack.append(evaluate(curr, 0, prevOp))
                
#                 curr = 0
#                 prevOp = c
#                 if c == ')':
#                     while type(stack[-1] == int):
#                         curr += stack.pop()
#                     prevOp = stack.pop()
                    
#         return sum(stack)
# #         stack = []
# #         curr = 0
# #         prevOp = "+"
# #         s += "@"
        
# #         for i in s:
# #             print(stack,i,prevOp)
# #             if i.isdigit():
# #                 curr = curr * 10 + int(i)
# #             elif i == '(':
# #                 stack.append(prevOp)
# #                 prevOp = "+"
# #             else:
# #                 if prevOp == "+":
# #                     stack.append(curr)
# #                 elif prevOp == '-':
# #                     stack.append(-curr)
# #                 elif prevOp == '*':
# #                     stack.append(stack.pop() * curr)
# #                 elif prevOp == '/':
# #                     stack.append(math.trunc(stack.pop() / curr))
# #                 curr = 0
# #                 prevOp = i 
# #                 if i == ')':
# #                     while type(stack[-1]) == int():
# #                         curr += stack.pop()
# #                     prevOp = stack.pop()
# #         print(stack)           
# #         return sum(stack)
        
class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(x, y, operator):
            if operator == "+":
                return x
            if operator == "-":
                return -x
            if operator == "*":
                return x * y
            return int(x / y)
        
        stack = []
        curr = 0
        previous_operator = "+"
        s += "@"
        
        for c in s:
            if c.isdigit():
                curr = curr * 10 + int(c)
            elif c == "(":
                stack.append(previous_operator)
                previous_operator = "+"
            else:
                if previous_operator in "*/":
                    stack.append(evaluate(stack.pop(), curr, previous_operator))
                else:
                    stack.append(evaluate(curr, 0, previous_operator))
                
                curr = 0
                previous_operator = c
                if c == ")":
                    while type(stack[-1]) == int:
                        curr += stack.pop()
                    previous_operator = stack.pop()

        return sum(stack)