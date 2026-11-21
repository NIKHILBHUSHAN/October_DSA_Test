class Solution:
    def maxProfit(self,prices):
        '''
        profit=0
        n=len(prices)
        for i in range(n):
            for j in range(i+1,n):
                current=prices[j]-prices[i]
                if current>profit:
                    profit=current
        return profit
        '''
        minPrice=prices[0]
        profit=0
        for i in range(1,len(prices)):
            current=prices[i]-minPrice
            if current>profit:
                profit=current
            if prices[i]<minPrice:
                minPrice=prices[i]
        return profit