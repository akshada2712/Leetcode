class Solution:
    def splitNum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        
        num1 = ''
        num2 = ''
        
        for i in range(len(num)):
            if i % 2 == 0:
                num1 += num[i]
            else:
                num2 += num[i]
                
        return int(num1) + int(num2)