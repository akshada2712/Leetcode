class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop(-1)
                
            ans = max(ans, len(stack))
            
        return ans
        