class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0 
        
        for index, num in enumerate(prices):
            if index == len(prices) -1:
                break 
            elif num < prices[index + 1]:
                max_profit += prices[index + 1] - num
                        
        return max_profit 
        
        
