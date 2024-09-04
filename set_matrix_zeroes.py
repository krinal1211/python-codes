class Solution(object):
    def setZeroes(self, matrix):
        m,n=len(matrix),len(matrix[0])
        row,col=(),()
        row,col=set(row),set(col)

        for i in range(m):
                for j in range(n):
                        if matrix[i][j]==0:
                                row.add(i)
                                col.add(j)
        for i in row:
                matrix[i]=n*[0]
        for i in col:
                for j in range(m):
                        matrix[j][i]=0
        return matrix
        
