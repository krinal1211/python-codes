from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0 
        sum_count = {0: 1} 
        sum = 0 
        for num in nums:
            sum += num  
            if sum - goal in sum_count:
                count += sum_count[sum - goal]
            sum_count[sum] = sum_count.get(sum, 0) + 1
        return count


# but timecomplexity is high
# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         i=0
#         sums=nums[i]
#         count=0
#         n=len(nums)
#         for i in range(n):
#             if nums[i]==goal:
#                 count+=1
               
#             sums=nums[i]
#             for j in range (i+1, n):
#                 if sums+nums[j]<=goal:
#                     sums += nums[j]
#                     if sums == goal:
#                         count += 1

#                 else:
#                     break
#         return count
#       
