#https://leetcode.com/problems/find-the-town-judge
class Solution:
    
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        graph = []
        for i in range(N + 1):
            graph.append([])
        for edge in trust:
            graph[edge[0]].append(edge[1])
        
        ind = 0
        for i in range(1, N + 1):
            if not graph[i]:
               ind = i
               break 
        
        for i in range(1, N + 1):
            if i != ind and ind not in graph[i]:
                return -1
        
        return ind    