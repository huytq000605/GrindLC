class Solution {
public:
    int dfs(vector<vector<int>> &dp, string &ring, string &key, int i, int j) {
        if(j >= key.size()) return 0;
        if(dp[i][j] != -1) {
            return dp[i][j];
        }
        int result = INT_MAX;
        for(int k = 0; k < ring.size(); k++) {
            if(ring[k] == key[j]) {
                int diff = abs(i - k);
                int cost = min(diff, int(ring.size()) - diff);
                result = min(result, dfs(dp, ring, key, k, j + 1) + cost + 1);
            }
        }
        dp[i][j] = result;
        return result;
    }
    int findRotateSteps(string ring, string key) {
        vector<vector<int>> dp(ring.size(), vector<int>(key.size(), -1));
        return dfs(dp, ring, key, 0, 0);
    }
};
