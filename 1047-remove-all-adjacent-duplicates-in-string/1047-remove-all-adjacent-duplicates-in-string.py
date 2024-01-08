class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append([i,1])
            else:
                stack[-1][1] += 1
            
            if stack[-1][1] == 2:
                stack.pop(-1)
        
        string = ""
        for i,j in stack:
            string += i * j
            
        return string
        