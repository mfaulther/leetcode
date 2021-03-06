//https://leetcode.com/problems/house-robber
class Solution {
public:
    int rob(vector<int>& nums) {
        int N = nums.size();
        if (N == 0)
            return 0;
        if (N == 1)
            return nums[0];
        vector<int> dp(N);
        dp[0] = nums[0];
        dp[1] = max(nums[0],nums[1]);
        for (int i = 2; i < N; i++)
        {
            dp[i] = max(dp[i-1],dp[i-2] + nums[i]);
        }
        
        return dp[N-1];
    }
};