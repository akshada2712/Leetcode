class Solution:
    def convertToBase7(self, num: int) -> str:
        remains = []
        if num == 0:
            return "0"
        
        if num < 0:
            isNeg = True
        else:
            isNeg = False
            
        num = abs(num)
      
        while num > 0:
            remains.append(str(num % 7))
            num //= 7
            
        if isNeg:
            return "-" + ''.join(remains[::-1])
           
        return ''.join(remains[::-1]) 
        