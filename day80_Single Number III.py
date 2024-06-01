class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        set_bit = xor_result & -xor_result
        
        uni1, uni2 = 0, 0
        for num in nums:
            if num & set_bit:
                uni1 ^= num
            else:
                uni2 ^= num
        
        return [uni1, uni2]
