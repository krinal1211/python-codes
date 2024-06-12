class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        curr = 0
        prev = 0
        end = len(nums) - 1

        while curr <= end:
            if nums[curr] == 0:
                nums[curr], nums[prev] = nums[prev], nums[curr]
                prev += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[end] = nums[end], nums[curr]
                end -= 1
            else:
                curr += 1

        return nums
        
