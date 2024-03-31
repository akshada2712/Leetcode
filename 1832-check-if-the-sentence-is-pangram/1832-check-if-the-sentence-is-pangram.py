class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
#         chkSet = set()
        
#         for i in sentence:
#             if i not in chkSet:
#                 chkSet.add(i)
        chkSet = set(sentence)
            
        return len(chkSet) == 26
        