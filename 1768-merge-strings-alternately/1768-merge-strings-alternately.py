class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        res = []
        
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        print(i,j)  
        while i != len(word1):
            res.append(word1[i])
            i += 1
            
        while j != len(word2):
            res.append(word2[j])
            j += 1
            
        return ''.join(res)
            
#         w1 = list(word1)
#         w2 = list(word2)
#         res = []
#         i = 0
#         w1.remove(w1[1])
#         while w1 and w2:
            
#             res.append(w1[i])
#             res.append(w2[i])
#             w1.remove(w1[i])
#             w2.remove(w2[i])
            
            
#         print(res)
            
        
        