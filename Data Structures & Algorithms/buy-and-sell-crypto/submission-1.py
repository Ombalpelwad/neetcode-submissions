class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        MaxProfit = 0
        for i in range(n):
            
            for j in range(i+1, n):
                if prices[i]<prices[j]:
                    profit = prices[j]-prices[i]
                    MaxProfit=max(MaxProfit,profit)
                    

        return MaxProfit
                