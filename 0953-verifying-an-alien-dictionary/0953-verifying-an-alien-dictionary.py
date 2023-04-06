class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # first differing character
        # if word A is prefix of word B, word B must be after word A
        
        orderIdx = {c:i for i , c in enumerate(order)}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            
            for j in range(len(w1)):
                if j == len(w2): # word2 is prefix of word1
                    return False
                
                if w1[j] != w2[j]:
                    if orderIdx[w2[j]] < orderIdx[w1[j]]:   # not sorted 
                        return False
                    break
                    
        return True
        