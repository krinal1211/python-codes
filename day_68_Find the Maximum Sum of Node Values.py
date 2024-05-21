class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        a=[(n^k) - n for n in nums]
        #  (n XOR k) and n ka diff
        a.sort(reverse=True)
        # for finding a max, and looping ki help se negative vala remove
        res=sum(nums)

        for i in range(0,len(nums),2):
            if i == len(nums) - 1:
                break
            path_a=a[i] +a[i+1]
            if path_a<=0:
                break
            res +=path_a
        return res
