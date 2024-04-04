class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        a=0
        for i in s:
            a=max(a,c)
            if i=="(":
                c=c+1
            elif i==")":
                c=c-1
        return a
        
