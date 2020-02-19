#https://leetcode.com/problems/power-of-two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        count = 0
        while (n):
            count += n % 2
            n = n//2
        return count == 1
