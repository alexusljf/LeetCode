class Solution:
    map = {}
    def climbStairs(self, n: int) -> int:
        if n in self.map:
            return self.map[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        steps = self.climbStairs(n - 1) + self.climbStairs(n - 2);
        self.map[n] = steps
        return steps