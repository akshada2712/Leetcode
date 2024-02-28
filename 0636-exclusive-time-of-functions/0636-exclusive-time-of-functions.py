class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack  = []
        res = [0] * n 
        
        for i in logs:
            id_, act, ts = i.split(":")
            
            id_ = int(id_)
            ts = int(ts)
            
            if act == 'start':
                stack.append((id_, ts))
            
            elif act == 'end':
                currId, currTs = stack.pop(-1)
                elapsedTime = ts + 1 - currTs
                
                res[currId] += elapsedTime 
                
                if stack:
                    res[stack[-1][0]] -= elapsedTime 
                    
        return res
            
        