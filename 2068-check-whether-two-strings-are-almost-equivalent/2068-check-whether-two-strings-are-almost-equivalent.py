class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c_w1 = Counter(word1)
        c_w2 = Counter(word2)
        common = set(word1 + word2)
        for char in common:
            if abs(c_w1[char] - c_w2[char]) > 3:
                return False
            
        return True