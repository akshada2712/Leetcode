class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                #print(i,w)
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    #print('in')
                    dp[i] = dp[i + len(w)]
                #print(dp)
                if dp[i]:
                    break
                    
        return dp[0]
        