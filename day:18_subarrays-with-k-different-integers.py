class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def fun(nums, k):
            count = 0
            start = 0
            freq = {}
            for end in range(len(nums)):
                freq[nums[end]] = freq.get(nums[end], 0) + 1
                while len(freq) > k:
                    freq[nums[start]] -= 1
                    if freq[nums[start]] == 0:
                        del freq[nums[start]]
                    start += 1
                count += end - start + 1
            return count
        
        return fun(nums, k) - fun(nums, k - 1)




# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
