class Solution {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        int MOD = 1e9 + 7;
        vector<int> arr;
        for(int b = 1; n; b <<= 1) {
            if(n & 1) arr.emplace_back(b);
            n >>= 1;
        }
        vector<vector<int>> c(arr.size(), vector<int>(arr.size()));
        for(int i = 0; i < arr.size(); ++i) {
            for(int j = i; j < arr.size(); ++j) {
                c[i][j] = (static_cast<long long>(i == j ? 1: c[i][j-1]) * arr[j]) % MOD;
            }
        }
        vector<int> result;
        for(auto &q: queries) {
            result.push_back(c[q[0]][q[1]]);
        }
        return result;
    }
};
