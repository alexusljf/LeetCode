class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in range(len(accounts)):
            cur = 0
            for j in range(len(accounts[i])):
                if i == 0:
                    max += accounts[i][j]
                else:
                    cur += accounts[i][j]
            if cur > max:
                max = cur
        return max
        