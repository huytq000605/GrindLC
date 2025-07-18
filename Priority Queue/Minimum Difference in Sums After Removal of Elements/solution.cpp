class Solution {
public:
    long long minimumDifference(vector<int>& nums) {
        int n = nums.size() / 3;
        priority_queue<int> left;
        priority_queue<int, vector<int>, decltype([](int n1, int n2) -> bool {
            return n1 > n2;
        })> right;
        long long sleft = 0, sright = 0;
        for(int i = 0; i < n; ++i) {
            left.emplace(nums[i]);
            sleft += nums[i];
            right.emplace(nums[3*n-1-i]);
            sright += nums[3*n-1-i];
        }
        vector<long long> dp(n+1);
        dp[0] = sleft;
        for(int i = n; i < 2 * n; ++i) {
            if(nums[i] < left.top()) {
                sleft += nums[i] - left.top();
                left.pop();
                left.emplace(nums[i]);
            }
            dp[i-n+1] = sleft;
        }
        long long result = sleft - sright;
        for(int i = 2*n-1; i >= n; --i) {
            if(nums[i] > right.top()) {
                sright += nums[i] - right.top();
                right.pop();
                right.emplace(nums[i]);
            }
            result = min(result, dp[i-n] - sright);
        }
        return result;
    }
};
