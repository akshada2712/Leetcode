class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        currPro = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                pro = prices[r]-prices[l]
                currPro += pro
                #print(currPro)
            l += 1
            r += 1
        return currPro
            
            
        