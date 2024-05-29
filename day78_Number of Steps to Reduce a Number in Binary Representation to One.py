class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        def find(d,c):
            if d==1:
                return c
            return find(d//2,c+1) if d%2==0 else find(d+1,c+1)
        return find(int(s,2),0)
        
