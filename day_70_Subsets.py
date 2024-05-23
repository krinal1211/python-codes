class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        self.a=[[]]
        def back(index,subset):
            if index==n:
                return
            self.a.append(subset + [nums[index]])

            # # for the checking
            # print(index,".......",subset ,"........", [nums[index]],"........",self.a)

            back(index+1,subset +[nums[index]])
            back(index+1,subset)
        back(0,[])
        return self.a
        
