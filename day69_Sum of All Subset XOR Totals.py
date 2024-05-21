class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def backtrack(index, current_xor):
            if index == len(nums):
                self.total_sum += current_xor
                return
            backtrack(index + 1, current_xor ^ nums[index])
            backtrack(index + 1, current_xor)
        
        self.total_sum = 0
        backtrack(0, 0)
        return self.total_sum
