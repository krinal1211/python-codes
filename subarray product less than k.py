class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=1:
            return 0 
        count = 0
        product = 1
        start= 0
        end=0
        n=len(nums)
        while(end<n):
            product*=nums[end]
            while(product>=k):
                product/=nums[start]
                start+=1
            count=count+(end-start)+1
            end+=1
        return count


# class Solution(object):
#     def numSubarrayProductLessThanK(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         count=0
#         for val in nums:
#             if val<k:
#                 count+=1
#         n=len(nums)
#         for i in range(n):
#             summ=nums[i]
#             m=1
#             for j in range(i+m,n):
#                 if summ*nums[j]<k:
#                     print(summ,nums[j])
#                     count+=1
#                     summ=summ*nums[j]
#                     m=m+1
#                 else:
#                     break
#         return count

        


        

        
