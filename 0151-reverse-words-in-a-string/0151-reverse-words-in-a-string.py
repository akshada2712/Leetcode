class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        print(lst)
        return ' '.join(lst[::-1])
#         print(lst)
#         print(lst[::-1])
#         lst = lst[::-1]
        
#         l = 0
        
#         while lst[l] != '' and l < len(s):
#             print(l)
#             lst.remove(lst[l])
#             l += 1
        
#         r = len(s) - 1
#         while lst[r] != '' and r >= 0:
#             lst.remove(lst[r])
#             r -= 1
#         print(lst)
#         return ' '.join(lst[::-1])
        