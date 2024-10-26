class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        currNum = 0
        res = 0
        pre_op = '+'
        s += '+'
        
        for i in s:
            if i.isdigit():
                currNum = currNum * 10 + int(i)
            elif i == ' ':
                pass 
            else:
                if pre_op == '+':
                    stack.append(currNum)
                elif pre_op == '-':
                    stack.append(-currNum)
                elif pre_op == '*':
                    stack.append(stack.pop() * currNum)
                elif pre_op == '/':
                    stack.append(math.trunc(stack.pop() / currNum))
                currNum = 0
                pre_op = i 
        return sum(stack)
                    
        