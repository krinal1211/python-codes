class Solution(object):
    def longestIdealString(self, s, k):
        dp = {}  
        for i in range(len(s)):
            max_length = 0
            for j in range(ord(s[i]) - k, ord(s[i]) + k + 1):
                if chr(j) in dp:
                    max_length = max(max_length, dp[chr(j)])
            dp[s[i]] = max_length + 1

        return max(dp.values())


