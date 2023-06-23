class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last = {}
        
        # create a hashmap which stores the last occurence of the character in string
        
        for i in range(len(s)):
            last[s[i]] = i
            
        #print(last)  # {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
        
        end = 0
        size = 0
        
        # defined two variables end and size
        # update end while iterating with its max(end, last(char))
        # if at any point end becomes equal to the idx it means a partition
        
        for i in range(len(s)):
            end = max(end, last[s[i]])
            size += 1
            if end == i:
                res.append(size)
                size = 0
                
        return res
            
        