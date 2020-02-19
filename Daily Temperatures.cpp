//https://leetcode.com/problems/daily-temperatures
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size());
        stack<int> st;
        st.push(0);
        for (int i = 1; i < T.size(); i++)
        {
            while (!st.empty() && T[st.top()] < T[i])
            {
                int curr = st.top();
                res[curr] = i - curr;
                st.pop();
            }
            st.push(i);
        }
        return res;
    }
};