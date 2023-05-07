class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        
        # numTree(4) = numtrees[0] * numtress[3]
        
        
        # 0 nodes - 1 tree
        # 1 node = 1 tree
        for nodes in range(2,n+1):
            tot = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                tot += dp[left] * dp[right]
            dp[nodes] = tot
            
        return dp[n]
                
        
        