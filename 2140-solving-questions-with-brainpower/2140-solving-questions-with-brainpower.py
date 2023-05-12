class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        
        for i in range(n-1, -1,-1):
            pts, bp = questions[i]
            
            next_q = min(bp + i + 1, n)
            pts_q = pts + dp[next_q]
            dp[i] = max(dp[i+1], pts_q)
            
        return dp[0]
        