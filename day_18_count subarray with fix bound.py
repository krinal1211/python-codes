class Solution:
    def countSubarrays(self, nums, minK, maxK):
        n = len(nums)
        l = -1
        Min,Max=-1,-1
        c=0

        for i in range(n):
            if nums[i]>=minK and nums[i]<=maxK:
                if nums[i]==minK :
                    Min=i
                else:
                    Min=Min
                if nums[i]==maxK:
                    Max=i
                else:
                    Max=Max
                c+= max(0,min(Min,Max)-l)
            else:
                l=i
                Min=-1
                Max=-1
        return c
