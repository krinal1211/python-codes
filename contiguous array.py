class Solution(object):
    def findMaxLength(self, nums):
        n=len(nums)
        mapv={}
        mapv[0]=-1
        maxlen=0
        val0=0
        val1=0
        for i in range(n):
            if nums[i]==0:
                val0 += 1
            else:
                val1 += 1
            if val1-val0 in mapv :
                diff=val1-val0
                maxlen=max(maxlen,i-mapv[diff])
            else:
                mapv[val1-val0]=i
        return maxlen
        
        
        
