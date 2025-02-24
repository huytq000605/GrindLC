class Solution {
public:
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n = edges.size() + 1;
        vector<vector<int>> tree(n);
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1];
            tree[u].emplace_back(v);
            tree[v].emplace_back(u);
        }
        auto dfs = [&](this auto&& dfs, int u, int p, int da) -> pair<int, int> {
            int db = u == bob ? 0: n;
            int earn{INT_MIN};
            for(int v: tree[u]) {
                if(v == p) continue;
                auto [nearn, ndb] = dfs(v, u, da+1);
                db = min(db, ndb);
                earn = max(earn, nearn);
            }
            if(earn == INT_MIN) earn = 0;
            if(da < db) earn += amount[u];
            else if(da == db) earn += amount[u] / 2;
            return {earn, db+1};
        };
        return dfs(0, -1, 0).first;
    }
};
