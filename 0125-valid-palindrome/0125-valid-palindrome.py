class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = [c for c in s.lower() if c.isalnum()]
        
        return new_s == new_s[::-1]
#         s = s.lower()
#         for i in s:
#             if i.isalnum() == False or i == ' ':
#                 s.replace(i,'')
#             elif i.isupper():
#                 s.replace(i,i.lower())
                
#         print(s)
        