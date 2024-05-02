class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxx(nums):
            if not nums:
                return -1

            max_val = max(nums)
            if -max_val in nums:
                return max_val
            else:
                nums.remove(max_val)
                return maxx(nums)

        return maxx(nums)
