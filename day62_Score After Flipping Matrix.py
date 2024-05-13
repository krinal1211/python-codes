class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m - count_ones:
                for i in range(m):
                    grid[i][j] ^= 1
        score = sum(int(''.join(map(str, row)), 2) for row in grid)
        return score

