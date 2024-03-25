class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=set()
        listt=[]
        for i in nums:
            if i in new:
                if i not in listt:
                    listt.append(i)
            else:
                new.add(i)
        return listt

        
