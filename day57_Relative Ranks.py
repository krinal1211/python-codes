class Solution(object):
    def findRelativeRanks(self, score):
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        n = len(score)
        temp = sorted(score, reverse=True)
        dir = {}
        for i in range(min(3, n)):
            dir[temp[i]] = ranks[i]
        for i in range(3, n):
            dir[temp[i]] = str(i + 1)
        
        return [dir[score[i]] for i in range(n)]
