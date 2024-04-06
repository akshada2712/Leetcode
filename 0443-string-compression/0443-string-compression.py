class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            runLen = 1
            while i + runLen < len(chars) and chars[i + runLen] == chars[i]:
                runLen += 1
            
            chars[res] = chars[i]
            res += 1
            if runLen > 1:
                chars[res:res+len(str(runLen))] = list(str(runLen))
                res += len(str(runLen))
                
            i += runLen
        return res