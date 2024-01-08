class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = collections.defaultdict(int)
        pairs = 0
        
        for t in time:
            if t % 60 == 0:
                pairs += hashmap[0]
            else:
                pairs += hashmap[60 - t%60]
            
            hashmap[t%60] += 1
            #print(t,hashmap)
            
        return pairs
#         pairs = 0
#         m = len(time)
#         hashmap = set()
#         for i in range(m):
#             for j in range(i+1,m):
#                 if (time[i] + time[j]) % 60 == 0 and (i,j) not in hashmap and (j,i) not in hashmap:
#                     pairs += 1
#                     hashmap.add((i,j))
#         #print(hashmap)            
#         return pairs
        