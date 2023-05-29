class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque([startGene])
        if endGene not in bank:
            return -1
        
        cnt = 0
        visit = set()
        
        options = ['A', 'C', 'G', 'T']
        visit.add(startGene)
        
        while q:
            size = len(q)
            
            for i in range(size):
                gene = q.popleft()
                if gene == endGene:
                    return cnt
                for j in range(8):
                    for opt in options:
                        newGene = gene[:j] + opt + gene[j+1:]
                        if newGene in bank and newGene not in visit:
                            visit.add(newGene)
                            q.append(newGene)
            cnt += 1
            
        return -1
                
        
        