class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for i in operations:
            if i == '+' and len(stack) >= 2:
                num = stack[-1] + stack[-2]
                stack.append(num)
            elif i == 'D' and len(stack) >= 1:
                stack.append(stack[-1] * 2)
            elif i == 'C' and len(stack) >= 1:
                stack.pop()
            else:
                stack.append(int(i))
                
        return sum(stack)