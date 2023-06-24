class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        target_sum = sum(arr)
        #(target_sum)
        if target_sum % 3 != 0 :
            return False
        
        target = target_sum // 3
        currSum = 0
        cnt = 0
        for i in arr:
            currSum += i
            if currSum == target:
                
                if cnt == 2:
                    return True
                currSum = 0
                cnt += 1
                
        return False
        
        