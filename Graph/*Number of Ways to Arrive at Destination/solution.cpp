class Solution {
int MOD = pow(10, 9) + 7;
public:
    int countPaths(int n, vector<vector<int>>& roads) { 
        vector<vector<pair<int, int>>> graph(n);
        for(auto& road: roads) {
            int u = road[0], v = road[1], w = road[2];
            graph[u].emplace_back(v, w);
            graph[v].emplace_back(u, w);
        }
        vector<long long> ds(n, LLONG_MAX);
        ds[0] = 0;
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, decltype([](auto& p1, auto& p2) {
            return p1.first > p2.first;
        })> pq;
        vector<int> ways(n);
        ways[0] = 1;
        pq.emplace(0, 0);
        while(!pq.empty()) {
            auto [t, u] = pq.top(); pq.pop();
            if(u == n-1) return ways[n-1];
            if(t > ds[u]) continue;
            for(auto [v, w]: graph[u]) {
                long long nt = t + w;
                if(nt < ds[v]) {
                    ways[v] = ways[u];
                    ds[v] = nt;
                    pq.emplace(nt, v);
                } else if(nt == ds[v]) {
                    ways[v] = (ways[u] + ways[v]) % MOD;
                }
            }
        }
        return 0;
    }
};
