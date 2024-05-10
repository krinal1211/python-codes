class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(arr)
        a=[]
        if len(arr)==2:
            return arr
        for i in range(n-1):
            for j in range(n-1,i,-1):
                a.append([arr[i]/float(arr[j]),arr[i],arr[j]])
        a.sort()
        return [a[k-1][1],a[k-1][2]]
                



             


        
