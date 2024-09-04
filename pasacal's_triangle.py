class Solution(object):
    def generate(self,numRows):
        arr=[[1]]
        def fun(i):
            temp=[1]*(i+1)
            for j in range(1,i):
                temp[j]=arr[i-1][j-1]+arr[i-1][j]
            return temp
        for i in range(1,numRows):
            arr.append(fun(i))
        return arr
