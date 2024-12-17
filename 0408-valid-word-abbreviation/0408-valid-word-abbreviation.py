class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        word_ptr = abbr_ptr = 0 
        
        
        while word_ptr < len(word) and abbr_ptr < len(abbr):
            
            if abbr[abbr_ptr].isdigit():
                steps = 0 
                
                if abbr[abbr_ptr] == '0':
                    return False 
                
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit(): 
                    steps = steps * 10 + int(abbr[abbr_ptr])
                    
                    abbr_ptr += 1
                    
                word_ptr += steps 
            else: 
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False 
                
                word_ptr += 1
                abbr_ptr += 1
                
        if word_ptr == len(word) and abbr_ptr == len(abbr):
            return True
        else:
            return False
#         i = 0 
        
#         while i < len(abbr):
#             step = ''
#             if abbr[i].isalpha():
#                 start = i
                
#             else:
#                 while abbr[i].isdigit():
#                     step += abbr[i]
#                     i += 1
#                 step = int(step)
#                 end = i+1
                
#             if abbr[start] == word[start] and abbr[end] == word[end+step]:
#                 continue 
#             else:
#                 return False 
            
#             i = i + end 
            
#         return True 
        