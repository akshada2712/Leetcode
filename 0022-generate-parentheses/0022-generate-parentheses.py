class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # using backtracking and keeping count of open and close paranethesis 
        # check if close_count < open_count : which gives choice to add eithwr open or close paranthesis 
        
        # only add open if open < n
        # only add close if close < open 
        # valid iff open == closed == n 
        
        stack = []
        res = []  # valid paranthesis 
        
        # use bactrack - called recursicely 
        
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return 
            
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closeN)
                stack.pop()
                
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
                
        backtrack(0, 0)
                
        return res 
            
            
        