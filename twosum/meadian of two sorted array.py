class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for i in nums2:
            nums1.append(i)
            nums1=sorted(nums1)
        if len(nums1)%2!=0:
            m=len(nums1)//2
            median=nums1[m]          
        else:
            m=len(nums1)//2
            mid=(nums1[m-1]+nums1[m])/2.0
            median=mid
        return median
c=Solution()
x=c.findMedianSortedArrays([1,2],[3,4])
print("{:.5f}".format(x))
