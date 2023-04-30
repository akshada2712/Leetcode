class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        
        while i <= j and i < len(s) and j > 0:
            # print(i,j)
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        
        return s