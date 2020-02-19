#https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
            res = 0
            jewels = set(J)
            for x in S:
                if x in jewels:
                    res += 1
    
            return res