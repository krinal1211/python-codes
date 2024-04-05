class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        n=len(s)
        while(i<n-1):
            val=abs(ord(s[i])- ord(s[i+1]))
            if val==32:
                s= s[:i] + s[i+2:]
                n=len(s)
                i=0
            else:
                i=i+1
        return s
            
        
