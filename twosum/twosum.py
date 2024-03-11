class Solution(object):
    def twoSum(self,nums,target):
         i=0
         j=0
         n=len(nums)
         flag=False
         for i in range (n):
             for j in range(i+1,n):
                 summ=nums[i]+nums[j]
                 if summ==target:
                     flag=True
                     return [i,j]
             if flag==True:
                 return
            
a=Solution()
a.twoSum([2,5,5,15],10)
