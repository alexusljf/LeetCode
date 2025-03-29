class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy at l, expand window with r. if lower l, set l to that
        l=0
        res = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            profit = prices[r] - prices[l]
            res = max(profit, res)
        return res
        