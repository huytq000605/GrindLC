class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        vector<unordered_map<int, int>> graph(n, unordered_map<int, int>());
        for(auto &edge: edges) {
            int v = edge[0], u = edge[1], w = edge[2];
            if(graph[u].find(v) == graph[u].end()) graph[u][v] = w;
            else graph[u][v] = min(graph[u][v], w);
        }
        function<bool(int)> valid = [&](int k) {
            vector<int> visited(n);
            visited[0] = 1;
            deque<int> dq{0};
            while(!dq.empty()) {
                int u = dq.front(); dq.pop_front();
                for(auto [v, w]: graph[u]) {
                    if(visited[v] || w > k) continue;
                    visited[v] = 1;
                    dq.emplace_back(v);
                }
            }
            
            for(int u{}; u < n; ++u) if(!visited[u]) return false;
            return true;
        };
        
        int lo{1}, hi{1000001};
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if(valid(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        
        return lo == 1000001 ? -1: lo;
    }
};
