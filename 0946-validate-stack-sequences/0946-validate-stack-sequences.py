class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        j = 0
        
        for i in range(len(pushed)):
            stack.append(pushed[i])
            
            while stack != [] and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            
        return True if len(stack) == 0 else False
        
        
        
#         stack = []
#         while len(pushed) != 0:
#             stack.append(pushed[0])
#             pushed.pop(0)
            
#             if stack[-1] == popped[0]:
#                 stack.pop(-1)
#                 popped.pop(0)
                
#         return True if len(stack) == 0 else False
        