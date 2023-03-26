class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        def get_len(i,length):
            if i == -1:
                return -1
            if i in visit:
                return -1
            
            if i in curr_seen:
                return length - curr_seen[i] + 1
            
            curr_seen[i] = length + 1
            
            return get_len(edges[i],length+1)
        
        res = -1
        visit = {}
        for i in range(len(edges)):
            curr_seen = {}
            length = get_len(i,0)
            res = max(res, length)
            visit |= curr_seen
            
        return res