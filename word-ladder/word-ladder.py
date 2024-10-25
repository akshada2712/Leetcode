class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = collections.defaultdict(list)
        
        wordList.append(beginWord)
        for w in wordList:   
            for j in range(len(w)):
                pattern = w[:j] + '*' + w[j+1:]   # building pattern 
                graph[pattern].append(w)
                
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1 
                
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiword in graph[pattern]:
                        if neiword not in visit:
                            q.append(neiword)
                            visit.add(neiword)
                            
            res += 1
            
            
        return 0
        