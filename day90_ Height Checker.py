class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sort_hei=sorted(heights)
        n=len(heights)
        c=0
        for i in range (n):
            print(i)
            if heights[i]!=sort_hei[i]:
                c=c+1
        return c
        
