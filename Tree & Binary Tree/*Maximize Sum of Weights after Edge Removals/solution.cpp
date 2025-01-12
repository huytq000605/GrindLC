class Solution {
public:
    long long maximizeSumOfWeights(vector<vector<int>>& edges, int k) {
        vector<vector<pair<int, int>>> tree(edges.size() + 1);
        for(auto &e: edges) {
            int u = e[0], v = e[1], w = e[2];
            tree[u].emplace_back(v, w);
            tree[v].emplace_back(u, w);
        }
        
        // returns [max weight having at most k children, max weight having at most k-1 children]
        auto dfs = [&](int u, int p, auto dfs) -> pair<long long, long long> {
            priority_queue<int, vector<int>, greater<int>> pq;
            long long res{};
            for(auto [v, w]: tree[u]) {
                if(v == p) continue;
                auto [a, b] = dfs(v, u, dfs);
                res += a;
                pq.emplace(max(0ll, b + w - a));
                if(pq.size() > k) pq.pop();
            }
            int mn{};
            if(pq.size() == k) {
                mn = pq.top();
                pq.pop();
            }
            while(!pq.empty()) {
                res += pq.top();
                pq.pop();
            }
            return {res + mn, res};
        };

        return dfs(0, -1, dfs).first;
    }
};
