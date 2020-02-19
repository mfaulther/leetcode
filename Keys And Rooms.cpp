//https://leetcode.com/problems/keys-and-rooms
class Solution {
public:
    void dfs(vector<vector<int>> & graph, vector<bool> & visited, int & count, int i)
{
		visited[i] = true;
        count++;
		for (int x : graph[i])
		{
            if (!visited[x])
			   dfs(graph,visited,count, x);
		}
}

bool canVisitAllRooms(vector<vector<int>>& rooms) {
	int N = rooms.size();
	vector<bool> visited(N,false);
    int count = 0;
	dfs(rooms,visited, count, 0);
	return count = rooms.size();

   }
};