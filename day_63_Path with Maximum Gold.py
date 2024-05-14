class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        def dfs(i,j,pathval):
            if i<0 or i>=len(grid) or j<0 or len(grid[0])<=j or grid[i][j]==0:
                return pathval
            # pathval=grid[i][j]+pathval     , it increase the TC
            gold= grid[i][j]
            grid[i][j]=0
            
            
            max_path=max(
                dfs(i + 1, j,pathval+gold),
                dfs(i - 1, j,pathval+gold),
                dfs(i, j + 1,pathval+gold),
                dfs(i, j - 1,pathval+gold))
            grid[i][j]=gold
            return max_path
        max_path=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    max_path=max(max_path,dfs(i,j,0))
        return max_path


