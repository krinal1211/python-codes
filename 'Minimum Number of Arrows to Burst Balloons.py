class Solution(object):
    def findMinArrowShots(self, points):
        points.sort()
        n=len(points)
        arrows=1
        if n==1:
            return 1
        for i in range(1,n):
            if points[i][0]>points[i-1][1]:
                arrows+=1
            else:
                points[i][0]=max(points[i][0],points[i-1][0])
                points[i][1]=min(points[i][1],points[i-1][1])
        return arrows
