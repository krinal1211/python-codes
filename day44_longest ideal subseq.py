class Solution(object):
    def longestIdealString(self, s, k):
        n = len(s)
        dp = [[0] * 26 for _ in range(n)]

        for i in range(n):
            for j in range(26):
                if i == 0:
                    dp[i][j] = 1 if ord(s[i]) - ord('a') == j else 0
                else:
                    diff = abs(ord(s[i]) - ord('a') - j)
                    if diff <= k:
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j-diff]) + 1
                    else:
                        dp[i][j] = dp[i-1][j]

        return max(max(row) for row in dp)
