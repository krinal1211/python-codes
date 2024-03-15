class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        sufix=[1]*n
        result=[]
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            sufix[j]=sufix[j+1]*nums[j+1]
        for k in range (n):
            result.append(prefix[k]*sufix[k])
        return result 
