//https://leetcode.com/problems/valid-parentheses
class Solution {
public:
    bool isValid(string s) {
        int N = s.size();
        stack<int> S;
        for (int i = 0; i < N; i++)
        {
            if (S.empty())
            {
                S.push(s[i]);
                continue;
            }
            if (s[i] == ')' && S.top() == '(' || s[i] == '}' && S.top() =='{' || s[i] == ']' && S.top() == '[')
            {
                S.pop();
            }
            else
            {
                S.push(s[i]);
            }
        }
        
        return S.empty();
    }
};