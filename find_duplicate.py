class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums=set()
        # here we are not use a list, use set  because when we find " if statement " it is take o(1) instante of o(n)
        for i in nums:
            if i in new_nums:
                return i
            else:
                new_nums.add(i)

        
