class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # less time complexity approach
        
        good = set()
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
                
            for i,v in enumerate(t):
                if v == target[i]:
                    good.add(i)
                    
        return len(good) == 3
            
        
        
        # property of max -> if any element in any triplets is greater than that indexed element in target then 
        # we need to pop off that triplet 
        # after that create three diff lists with 1st, 2nd, 3rd elements from the remaining triplet and then 
        # chk if target is there. if not return False
        
        
#         i = 0
#         while True:
#             if i == len(triplets):
#                 break
                
#             for j in range(3):
#                 if triplets[i][j] > target[j]:
#                     triplets.pop(i)
#                     i -= 1
#                     break
                    
#             i += 1
            
#         a = [x[0] for x in triplets]
#         b = [x[1] for x in triplets]
#         c = [x[2] for x in triplets]
        
#         if target[0] not in a:
#             return False
        
#         if target[1] not in b:
#             return False


#
        
#         if target[2] not in c:
#             return False
        
#         return True
        