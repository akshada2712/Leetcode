class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackt = []
        
        for i in s:
            if i == '#':
                if stackS:
                    stackS.pop(-1)
            else:
                stackS.append(i)
                
        for i in t:
            if i == '#':
                if stackt:
                    stackt.pop(-1)
            else:
                stackt.append(i)
        print(stackt, stackS)       
        return stackS == stackt
                
                
                
        