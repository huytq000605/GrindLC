class Solution {
public:
    int minTransfers(vector<vector<int>>& transactions) {
        vector<int> balance(12);
        for(auto& txn: transactions) {
            int u = txn[0], v = txn[1], w = txn[2];
            balance[u] -= w;
            balance[v] += w;
        }   
        auto dfs = [&](this auto&& dfs, int i) {
            if(i >= 12) return 0;
            if(!balance[i]) return dfs(i+1);
            int result = INT_MAX;
            for(int j = i+1; j < 12; ++j) {
                if(!balance[j] || balance[j] * balance[i] > 0) continue;
                balance[j] += balance[i];
                result = min(result, 1 + dfs(i+1));
                balance[j] -= balance[i];
            }
            return result;
        };
        return dfs(0);
    }
};
