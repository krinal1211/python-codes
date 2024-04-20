class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        if not land:
            return []

        def dfs(i, j, bottom_right):
            if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or land[i][j] == 0:
                return bottom_right
            land[i][j] = 0
            bottom_right[0] = max(bottom_right[0], i)
            bottom_right[1] = max(bottom_right[1], j)
            bottom_right = dfs(i + 1, j, bottom_right)
            bottom_right = dfs(i - 1, j, bottom_right)
            bottom_right = dfs(i, j + 1, bottom_right)
            bottom_right = dfs(i, j - 1, bottom_right)
            return bottom_right

        groups = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    top_left = [i, j]
                    bottom_right = [i, j]
                    bottom_right = dfs(i, j, bottom_right)
                    groups.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])
        return groups
