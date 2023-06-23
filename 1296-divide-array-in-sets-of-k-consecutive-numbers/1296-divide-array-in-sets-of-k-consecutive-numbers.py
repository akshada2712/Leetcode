class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        count = Counter(nums)
        
        minH = list(count.keys())
        
        heapq.heapify(minH)
        
        while minH:
            first = minH[0]
            
            for i in range(first, first + k):
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
                    
        return True
                
        