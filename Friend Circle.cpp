//https://leetcode.com/problems/friend-circles
class Solution {
public:
    
    int find(vector<int> parent,int i)
   {
	  if (parent[i] == i)
		  return i;
	  return find(parent,parent[i]);
   }

    //union
    void un(vector<int> & parent, int i, int j)
  {
	  int pi = find(parent, i);
	  int pj = find(parent, j);
	  parent[pi] = pj;
  }
    int findCircleNum(vector<vector<int>>& M) {
    int N = M.size();
    int res = N;
	
    bool b = true;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (M[i][j] != 1)
            {
                b = false;
                break;
            }
        }
        if (!b)
            break;
    }
    if (b)
        return 1;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (M[i][j] == 1)
			   res --;
		}
	}   
    return res;
  }
};