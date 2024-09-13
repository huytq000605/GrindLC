class Solution {
public:
    vector<int> maximumSubarrayXor(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        // a b -> a ^ b
        // a b c -> (a^b) ^ (b^c)
        // a b c d -> (a^b) ^ (b^c) ^ (c^d) -> (a^b^b^c) ^ (b^c^c^d)
        // xor[i][j] = xor[i][j-1] ^ xor[i+1][j] 
        vector<vector<int>> x(n, vector<int>(n));
        for(int i = 0; i < n; ++i) {
            x[i][i] = nums[i];
        }
        for(int d = 1; d < n; ++d) {
            for(int i = 0; i < n - d; ++i) {
                int j = i + d;
                x[i][j] = x[i][j-1] ^ x[i+1][j];
            }
        }

        // xor[i][j] is created from xor[i][j-1] and xor[i+1][j]
        // so max value of xor[i][j] = max({x[i][j], x[i+1][j], x[i][j-1]})
        for(int d = 1; d < n; ++d) {
            for(int i = 0; i < n - d; ++i) {
                int j = i + d;
                x[i][j] = max({x[i][j], x[i+1][j], x[i][j-1]});
            }
        }

        vector<int> result;
        for(auto &q: queries) {
            result.emplace_back(x[q[0]][q[1]]);
        }
        return result;
    }
};
