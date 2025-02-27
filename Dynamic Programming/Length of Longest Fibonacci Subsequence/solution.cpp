class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        int n = arr.size();
        vector<vector<int>> dp(n, vector<int>(n));
        unordered_map<int, int> numi;
        int result{};
        for(int i{}; i < arr.size(); ++i) {
            numi[arr[i]] = i;
            for(int j{i-1}; j >= 0; --j) {
                int c = arr[i], b = arr[j], a = c - b;
                if(a > b || numi.find(a) == numi.end()) {
                    dp[i][j] = 1;
                    continue;
                }
                int k = numi[a];
                dp[i][j] = dp[j][k] + 1;
                result = max(result, dp[i][j]);
            }
        }
        if(result <= 1) return 0;
        return result+1;
    }
};
