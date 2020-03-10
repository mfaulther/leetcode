#https://leetcode.com/problems/longest-palindromic-subsequence/


#Top-Down Dynamic Programming
def helper(s: str, i: int, j: int, d: dict):
    if i > j:
        return 0
    if (i, j) in d:
        return d[(i, j)]
    else:
        if i == j:
            return 1
        if s[i] == s[j]:
            d[(i, j)] = 2 + helper(s, i+1, j-1, d)
            return d[(i, j)]
        else:
            d[(i, j)] = max(helper(s, i+1, j, d), helper(s, i, j-1, d))
            return d[(i, j)]



def longestPalindromeSubseq(s: str) -> int:
    D = {}
    return helper(s, 0, len(s) - 1, D)


#0123456
#efbcabe


#dp[0, 6] = dp[1, 5] + 2
#dp[1, 5] = max(dp[2,5], dp[1,4])


