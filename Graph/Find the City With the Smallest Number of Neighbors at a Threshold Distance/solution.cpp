class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int threshold) {
        vector<vector<pair<int, int>>> graph(n, vector<pair<int, int>>());
        for(auto e: edges) {
            auto u = e[0], v = e[1], w = e[2];
            graph[u].emplace_back(v, w);
            graph[v].emplace_back(u, w);
        }
        
        auto dijkstra = [&](int u) -> vector<int> {
            vector<int> distances(n, INT_MAX);
            priority_queue<pair<int, int>,
                vector<pair<int, int>>,
                decltype([](auto p1, auto p2) {
                    return p1.first > p2.first;
                })> pq;
            pq.emplace(0, u);
            distances[u] = 0;
            while(!pq.empty()) {
                auto [s, u] = pq.top();
                pq.pop();
                for(auto [v, w]: graph[u]) {
                    if(s + w < distances[v] && s + w <= threshold) {
                        distances[v] = s + w;
                        pq.emplace(s + w, v);
                    }
                }
            }
            return distances;
        };

        int city = 0, min_neighbors = 101;
        for(int u = 0; u < n; u++) {
            auto ds = dijkstra(u);
            int neighbors = 0;
            for(auto d: ds) {
                if(d != INT_MAX) neighbors += 1;
            }
            if(neighbors <= min_neighbors) {
                min_neighbors = neighbors;
                city = u;
            }
        }
        return city;
    }
};
