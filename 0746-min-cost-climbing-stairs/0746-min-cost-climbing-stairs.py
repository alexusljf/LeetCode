class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # base cases would be the first 2 items (either start at index 0 or 1)
        for i in range(2,len(cost)):
            # add the min cost to reach this step
            cost[i]+= min(cost[i-1], cost[i-2])
        # as u can take 1 or 2 steps, we return the min cost of reaching whichever of the top 2 steps
        return min(cost[-1], cost[-2])