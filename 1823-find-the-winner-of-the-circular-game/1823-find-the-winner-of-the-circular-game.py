class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        vals = [x for x in range(1,n+1)]
        ptr = k - 1
        
        while len(vals) != 1:
            if len(vals) <= ptr:
                ptr = ptr % len(vals)
                
            vals.pop(ptr)
            ptr += (k - 1)
            
        return vals[0]
        
#         l = 0 
#         r = l + 1 
#         k -= 1
        
#         while len(vals) != 1:
#             print(l,r, vals)
#             if r % k == 0:
#                 if r > len(A):
#                     r = 0
                    
#                 vals.pop(r)
#                 l = l + 1
#                 r = r + 1
#             else:
#                 r = r + 1 
                
#         print(vals)
            
            
        
        