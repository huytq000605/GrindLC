class Solution {
public:
    int findMaxPathScore(vector<vector<int>>& edges, vector<bool>& online, long long k) {
        int lo = 0, hi = 0;
        int n = online.size();
        vector<vector<pair<int, int>>> graph(n);
        vector<int> indegree(n);
        for(auto& e: edges) {
            int u = e[0], v = e[1], w = e[2];
            if(!online[u] || !online[v]) continue;
            graph[u].emplace_back(v, w);
            hi = max(hi, w);
            indegree[v] += 1; 
        }

        vector<int> topo;
        deque<int> dq{};
        for(int u = 0; u < n; ++u) if(!indegree[u]) dq.push_back(u);
        while(!dq.empty()) {
            int u = dq.front(); dq.pop_front();
            topo.push_back(u);
            for(auto [v, w]: graph[u]) {
                indegree[v]--;
                if(!indegree[v]) {
                    dq.push_back(v);
                }
            }
        }
        
        auto valid = [&](int threshold) -> bool {
            vector<long long> ds(n, k+1);
            ds[0] = 0;
            for(int u: topo) {
                if(ds[u] > k) continue;
                for(auto [v, w]: graph[u]) {
                    if(w < threshold || ds[u] + w >= ds[v]) continue;
                    ds[v] = ds[u] + w;
                }
            }
            return ds.back() <= k;
        };

        while(lo < hi) {
            int m = lo + (hi - lo + 1) / 2;
            if(valid(m)) {
                lo = m;
            } else {
                hi = m - 1;
            }
        }
        if(!valid(lo)) return -1;
        return lo;
    }
};
