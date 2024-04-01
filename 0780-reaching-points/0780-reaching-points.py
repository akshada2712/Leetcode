from collections import deque
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx == tx and sy == ty :
            return True 
        
        while tx >= sx and ty >= sy:
            if tx == ty:
                break 
            elif tx > ty :
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
                
        return tx == sx and ty == sy
            
        
        
        
        ## TLE
#         while tx >= sx and ty >= sy:
#             if tx == sx and ty == sy:
#                 return True 
#             else:
#                 if tx > ty:
#                     tx -= ty 
#                 else:
#                     ty -= tx 
                    
#         return False
        
#         q = deque()
#         q.append((sx, sy))
#         #seen = set((sx, sy))
        
#         # reverse operations 
        
#         while q:
#             x, y = q.popleft()
            
#             if x == sx and y == sy:
#                 return True
#             print(x,y)
            
#             elif x <= sx or y <= sy:
#                 continue
                
#             else:
#                 if x > y: 
#                     q.append((x, x - y))
#                     q.append((x -y, y))
#                 else:
#                     q.append((x, y -x))
#                     q.append(y - x, y)
                    
#         return False
        
        # this will give memory overflow error
#         while q:
#             x, y = q.popleft()
#             #print(x,y)
#             if x == tx and y == ty:
#                 return True
#             elif x > tx or y > ty:
#                 continue 
                
#             else:
#                 q.append((x, x + y))
#                 q.append((x + y, y))
                
#         return False
            
             
        