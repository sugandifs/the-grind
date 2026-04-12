class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(curr_profit, max_profit)

            sell += 1

        return max_profit


