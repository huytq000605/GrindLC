class Solution {
public:
    int minimumIncrements(vector<int>& nums, vector<int>& target) {
        int m = target.size();
        unordered_map<long long, long long> lcms;
        for(int mask{1}; mask < (1 << m); ++mask) {
            long long l = 1;
            for(int i{}; i < m; ++i) {
                if((mask >> i) & 1) {
                    if(l == 1) l = target[i];
                    else l = lcm(l, static_cast<long long>(target[i])); 
                }
            }
            lcms[mask] = l;
        }
        
        vector<long long> dp(1 << m, INT_MAX);
        dp[0] = 0;
        for(int num: nums) {
            vector<long long> ndp = dp;
            for(int prev_mask{}; prev_mask < (1 << m); ++prev_mask) {
                if(dp[prev_mask] == INT_MAX) continue;
                for(int mask{1}; mask < (1 << m); ++mask) {
                    long long l = lcms[mask];
                    int mod = num % l;
                    long long ops = (mod == 0) ? 0: l - mod;
                    ndp[prev_mask | mask] = min(ndp[prev_mask | mask], dp[prev_mask] + ops);
                }
            }
            dp = ndp;
        }
        return dp.back();
    }
};
