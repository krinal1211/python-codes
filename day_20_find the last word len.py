class Solution(object):
    def lengthOfLastWord(self, s):
        n=len(s)
        i=0
        c=0
        while(s[n-i-1]==" " and n-i>0):
            i=i+1
        while(s[n-i-1]!=" " and n-i>0):
            c=c+1
            i=i+1
        return c
     
        # listt=s.split()
        # n=len(listt)
        # return len(listt[n-1])
        
