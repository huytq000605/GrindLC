class Solution {
public:
    int minCost(int n, vector<vector<int>>& edges) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype([](auto &p1, auto &p2) -> bool {
            return p1.first > p2.first;
        })> pq;
        vector<int> ds(n, INT_MAX);
        ds[0] = 0;
        pq.emplace(0, 0);
        vector<vector<pair<int, int>>> graph(n);
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u].emplace_back(v, w);
            graph[v].emplace_back(u, w*2);
        }
        while(!pq.empty()) {
            auto [s, u] = pq.top(); pq.pop();
            if(u == n-1) return s;
            for(auto [v, w]: graph[u]) {
                if(s + w < ds[v]) {
                    ds[v] = s + w;
                    pq.emplace(s + w, v);
                }
            }
        }
        return -1;
    }
};
