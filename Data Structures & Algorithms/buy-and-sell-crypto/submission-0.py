class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0 
        n = len(prices)
        if n == 2 and prices[0] < prices[1]:
            return prices[1] - prices[0]
        elif n == 2 and prices[0] > prices[1] : 
            return 0
        else: 
            for i in range(n - 1):
                maxprice = max(prices[i+1::])
                if maxprice > prices[i]:
                    mp = max(mp,maxprice - prices[i])
                else:
                    continue
            return mp
            


        