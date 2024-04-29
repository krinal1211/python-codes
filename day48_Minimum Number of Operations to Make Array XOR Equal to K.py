class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        final_xor = 0
        for num in nums:
            final_xor ^= num
        
        count = 0
        while k > 0 or final_xor > 0:
            if k % 2 != final_xor % 2:
                count += 1
            k //= 2
            final_xor //= 2

        return count

