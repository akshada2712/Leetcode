class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        ctw = {}
        wtc = {}
        
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern,words):
            if c in ctw and ctw[c] != w:
                return False
            if w in wtc and wtc[w] != c:
                return False
            
            wtc[w] = c
            ctw[c] = w
            
        return True
        