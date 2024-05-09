class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        temp = sorted(happiness, reverse=True)
        c = 0
        i = 0

        for _ in range(k):
            i += 1
            maxx = temp.pop(0)
            if maxx <= 0:
                return c
            if not temp:
                return c + maxx
            c += maxx
            temp[0] -= i

        return c
# use with the recurtion
# class Solution(object):
#     def maximumHappinessSum(self, happiness, k):
#         """
#         :type happiness: List[int]
#         :type k: int
#         :rtype: int
#         """
#         temp=sorted(happiness,reverse=True)
#         c=0
#         i=0
#         def fun(temp,k,c,i):
#             i=i+1
#             maxx=temp.pop(0)
#             if k == 0 or maxx<=0:
#                 return c
#             if not temp:
#                 return c+maxx
#             c=c+maxx
#             temp[0]=temp[0]-i
#             return fun(temp,k-1,c,i)
#         return fun(temp,k,c,i)


        

        
