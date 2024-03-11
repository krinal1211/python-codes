class Solution(object):
    def customSortString(self, order, s):
        ns=list(s)
        result=""
        for i in order:
            for j in s:
                if i==j:
                    result+=j
                    ns.remove(j)
        x="".join(ns)
        result=result+x
        print(result)
        return result
order='cba'
s='abcd'
a=Solution()
a.customSortString( order, s)


       
        
