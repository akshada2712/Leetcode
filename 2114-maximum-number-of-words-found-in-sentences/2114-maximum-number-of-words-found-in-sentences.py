class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        runnMax = float("-inf")
        for i in sentences:
            runnMax = max(runnMax, len(i.split(" ")))
        
        return runnMax
        