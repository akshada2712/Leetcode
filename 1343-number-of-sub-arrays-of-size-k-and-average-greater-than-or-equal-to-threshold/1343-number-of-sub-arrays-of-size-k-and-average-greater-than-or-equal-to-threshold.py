class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        cnt = 0
        runSum = 0
        
        for r in range(len(arr)):
            runSum += arr[r]
            
            if (r - l + 1) == k:
                avg = runSum / k
                if avg >= threshold:
                    cnt += 1
                    
                runSum -= arr[l]
                l += 1
                
        return cnt
        