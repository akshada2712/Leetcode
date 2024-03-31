class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chkSet = set()
        
        for i in sentence:
            if i not in chkSet:
                chkSet.add(i)
            
        return True if len(chkSet) >= 26 else False
        