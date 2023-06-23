class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        if len(hand) % groupSize:
            return False
        for i in hand:
            count[i] = 1 + count.get(i,0)
        
        minH = list(count.keys())
        
        heapq.heapify(minH)
        
        while minH:
            first = minH[0]
            for i in range(first, groupSize + first):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
                    
                
                    
        return True
                        