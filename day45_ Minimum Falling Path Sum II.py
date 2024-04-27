class Solution(object):
    def minFallingPathSum(self, grid):
        size = len(grid)
        dp = grid[0][:]
        for i in range(1, size):
            new_dp = [float('inf')] * size
            for j in range(size):
                for k in range(size):
                    if j != k:
                        new_dp[j] = min(new_dp[j], dp[k] + grid[i][j])
            dp = new_dp
        return min(dp)
