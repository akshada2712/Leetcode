class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for i in asteroids:
            if i < 0:
                while stack and stack[-1] > 0:
                    j = stack.pop()
                    if abs(i) == abs(j):
                        break
                    elif abs(j) > abs(i):
                        stack.append(j)
                        break
                else:
                    stack.append(i)
                        
            else:
                stack.append(i)
                            
                
        return stack
    
    
    
        