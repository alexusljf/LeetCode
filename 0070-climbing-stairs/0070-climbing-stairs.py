class Solution:
    # top down way
    # map = {}
    # def climbStairs(self, n: int) -> int:
    #     if n in self.map:
    #         return self.map[n]
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     steps = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    #     self.map[n] = steps
    #     return steps

    # bottom down way
    def climbStairs(self, n:int) -> int:
        dp = [1,1]
        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]