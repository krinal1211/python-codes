class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  

        def dfs(i, j, k):
            print("i,j,k,: ",i,j,k)
            if k == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            temp, board[i][j] = board[i][j], ''
            
            for x, y in directions:
                print(x,y)
                print(i+x,j+y)
                if dfs(i + x, j + y, k + 1):
                    return True
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
