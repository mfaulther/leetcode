#https://leetcode.com/problems/longest-common-subsequence/

def longestCommonSubsequence(text1: str, text2: str) -> int:
    text1, text2 = '0' + text1, '0' + text2
    n, m = len(text1), len(text2)
    dp = [m*[0] for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n-1][m-1]