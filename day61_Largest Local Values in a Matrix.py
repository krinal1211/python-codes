class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        listt= []
        
        for i in range(1, n - 1):
            max_row = []
            for j in range(1, n - 1):
                submatrix = [
                    grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                    grid[i][j - 1], grid[i][j], grid[i][j + 1],
                    grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
                ]
                max_value = max(submatrix)
                max_row.append(max_value)
            listt.append(max_row)
        
        return listt

