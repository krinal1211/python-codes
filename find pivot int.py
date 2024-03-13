class Solution:
    def pivotInteger(self, n: int) -> int:  
        if n==1:
            return 1
        mid=n//2+1   
        c=n*(n+1)//2 
        while (mid<n-1):      
            a=mid*(mid+1)//2
            b=c-a+mid
            if a==b:
                return mid
            mid=mid+1
        return -1
