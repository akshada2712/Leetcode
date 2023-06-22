class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        res = []
        hashmap = Counter(s)
        
        maxHeap = []
        
        for val in hashmap:
            heapq.heappush(maxHeap, [-hashmap[val],val])
            
        while len(maxHeap) > 1:
            f1, c1 = heapq.heappop(maxHeap)
            f2, c2 = heapq.heappop(maxHeap)
            
            res.append(c1)
            res.append(c2)
            
            if abs(f1) > 1:
                heapq.heappush(maxHeap,[1+f1,c1])
                
            if abs(f2) > 1:
                heapq.heappush(maxHeap,[1+f2,c2])
                
        if maxHeap:
            f,c = maxHeap[0]
            # print(f,c)
            if abs(f) > 1:
                return ''
            else:
                res.append(c)
        return ''.join(res)
            
            