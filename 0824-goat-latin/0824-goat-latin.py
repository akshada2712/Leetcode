class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        words = sentence.split(' ')
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = []
        
        for i, word in enumerate(words):
            new_word = ''
            if word[0].lower() in vowels:
                new_word += word + 'ma'
                
            else: 
                new_word += word[1:] + word[0] + 'ma'
                
            # append a 
            new_word += ((i + 1 )* 'a')
            # print(new_word)
            
            ans.append(new_word)
            
        return ' '.join(ans)
                
                
        