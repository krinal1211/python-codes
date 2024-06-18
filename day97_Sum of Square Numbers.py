class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l=0
        summ=0
        r=int(sqrt(c))
        while(l<=r):
            summ=l*l+r*r
            if summ==c:
                return True
            if summ>c:
                r=r-1
            else:
                l=l+1
        
       
        
        
        
