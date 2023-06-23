class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last = {}
        
        for i in range(len(s)):
            last[s[i]] = i
            
        #print(last)  # {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
        
        end = 0
        size = 0
        
        
        for i in range(len(s)):
            end = max(end, last[s[i]])
            size += 1
            if end == i:
                res.append(size)
                size = 0
                
        return res
            
        