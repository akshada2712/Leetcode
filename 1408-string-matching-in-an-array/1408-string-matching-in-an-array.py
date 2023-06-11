class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        n = len(words)
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if words[j] in words[i]:
                    if words[j] not in res:
                        res.append(words[j])
                        
        return res
        