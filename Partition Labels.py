#https://leetcode.com/problems/partition-labels
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        last_pos = {}
        for i in range (len(S)):
            last_pos[S[i]] = i
        pos = 0
        while pos < len(S):
            m0 = pos
            m1 = last_pos[S[pos]]
            while pos < m1:
                pos += 1
                m1 = max(m1, last_pos[S[pos]])
            pos += 1
            res.append(pos - m0)
        return res