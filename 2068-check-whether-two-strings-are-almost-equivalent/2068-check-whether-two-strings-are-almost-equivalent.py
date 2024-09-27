class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        # use counter -> if the character is absent it will return 0 
        c_w1 = Counter(word1)
        c_w2 = Counter(word2)
        
        # we create a set which is union of all characters from both words, easy to iterate and handle edges cases for character not present in either of the words
        common = set(word1 + word2)
        for char in common:
            
            if abs(c_w1[char] - c_w2[char]) > 3:
                return False
            
        return True