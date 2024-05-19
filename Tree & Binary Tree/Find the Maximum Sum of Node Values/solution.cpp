class Solution {
public:
    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        int cnt = 0;
        int min_diff = INT_MAX;
        long long result = 0;
        for(int u = 0; u < n; u++) {
            int x = nums[u] ^ k;
            if(nums[u] < x) cnt++;
            min_diff = min(min_diff, abs(nums[u] - x));
            result += max(x, nums[u]);
        }
        if(cnt & 1) result -= min_diff;
        return result;
    }
};
