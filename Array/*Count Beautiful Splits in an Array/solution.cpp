class Solution {
public:
    int beautifulSplits(vector<int>& nums) {
        int n = nums.size();
        auto z = [&](int start) {
            vector<int> z(n, 0);
            int l{}, r{};
            for(int i{start+1}; i < n; ++i) {
                if(i < r) {
                    z[i] = min(r - i, z[start + i - l]);
                }
                while(i + z[i] < n && nums[i + z[i]] == nums[start + z[i]]) {
                    ++z[i];
                }
                if(i + z[i] > r) {
                    l = i;
                    r = i + z[i];
                }
            }
            return z;
        };
        vector<vector<int>> zs(n);
        for(int i{}; i < n; ++i) {
            zs[i] = z(i);
        }
        int result{};
        for(int i{1}; i < n-1; ++i) {
            for(int j{i+1}; j < n; ++j) {
                bool valid{};
                if(j-i>=i && zs[0][i] >= i) {
                    valid = true;
                }
                if(n-j >= j-i && zs[i][j] >= j-i) {
                    valid = true;
                }
                if(valid) ++result;
            }
        }
        return result;
    }
};
