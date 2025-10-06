class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest_price=prices[0]
        for i in range (0, len(prices)):
            if prices[i]<lowest_price:
                lowest_price = prices[i]
            
            if prices[i]-lowest_price>profit:
                    profit = prices[i]-lowest_price 

        return profit