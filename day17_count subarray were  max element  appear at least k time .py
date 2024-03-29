class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        window_start = 0
        max_count = 0
        max_num = max(nums)
        
        for window_end in range(len(nums)):
            if nums[window_end] == max_num:
                max_count += 1
            
            while max_count >= k:
                count += len(nums) - window_end
                if nums[window_start] == max_num:
                    max_count -= 1
                window_start += 1
        
        return count
