class Solution {
public:
    vector<long long> minCost(int n, vector<vector<int>>& roads, vector<int>& appleCost, int k) {
        vector<vector<pair<int, int>>> graph(n, vector<pair<int, int>>());
        for(auto road: roads) {
            int u = road[0]-1, v = road[1]-1, w = road[2];
            graph[u].emplace_back(v, w);
            graph[v].emplace_back(u, w);
        }
        vector<long long> result(n, INT_MAX);
        for(int start = 0; start < n; start++) {
            priority_queue<pair<int, long long>, vector<pair<int, long long>>, 
                decltype([](auto a, auto b) -> bool {
                    return a.second > b.second;
                })> pq;
            pq.emplace(start, 0);
            vector<long long> ds(n, INT_MAX);
            ds[start] = 0;
            while(pq.size() > 0) {
                auto [u, s] = pq.top();
                pq.pop();
                result[start] = min(result[start], appleCost[u] + s);
                for(auto [v, w]: graph[u]) {
                    if(s + (k + 1) * w < ds[v]) {
                        ds[v] = s + (k+1) * w;
                        pq.emplace(v, s + (k + 1) * w);
                    }
                }
            }
        }
        return result;
    }
};
