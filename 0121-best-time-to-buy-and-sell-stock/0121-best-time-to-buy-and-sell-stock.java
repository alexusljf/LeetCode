class Solution {
    public int maxProfit(int[] prices) {
        // get lowest price, then highest price that occurs AFTER the lowest
        // use 2 pointers to compare prices in 1 loop
        int left = 0, right = 1, maxProfit = 0, profit = 0;
        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                profit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, profit);
            } else {
                left = right;
            }
            right++;
        }
        return maxProfit;
    }
}