class Solution {
public:
    int maxValue(vector<int>& nums, int k) {
        int n = nums.size();
        
        vector<int> i1(1<<7, n);
        vector<vector<vector<int>>> dp1(n, vector<vector<int>>(k+1, vector<int>(1<<7, 1)));
        auto dfs1 = [&](int i, int k, int mask, auto dfs_ref) -> void {
            if(k == 0) {
                i1[mask] = min(i1[mask], i-1);
            } else if(i < n && dp1[i][k][mask]) {
                dp1[i][k][mask] = 0;
                dfs_ref(i+1, k-1, mask | nums[i], dfs_ref);
                dfs_ref(i+1, k, mask, dfs_ref);
            }
        };
        dfs1(0, k, 0, dfs1);
        
        vector<int> i2(1<<7, -1);
        vector<vector<vector<int>>> dp2(n, vector<vector<int>>(k+1, vector<int>(1<<7, 1)));
        auto dfs2 = [&](int i, int k, int mask, auto dfs_ref) -> void {
            if(k == 0) {
                i2[mask] = max(i2[mask], i+1);
            } else if(i >= 0 && dp2[i][k][mask]) {
                dp2[i][k][mask] = 0;
                dfs_ref(i-1, k-1, mask | nums[i], dfs_ref);
                dfs_ref(i-1, k, mask, dfs_ref);
            }
        };
        dfs2(n-1, k, 0, dfs2);
        
        int result = 0;
        for(int left = 0; left < 1<<7; ++left) {
            for(int right = 0; right < 1<<7; ++right) {
                if(i1[left] < i2[right]) {
                    result = max(result, left ^ right);
                }
            }
        }
        return result;
    }
};
