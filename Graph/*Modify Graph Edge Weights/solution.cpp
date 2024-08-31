class Solution {
public:
    vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges, int source, int destination, int target) {
        vector<map<int, int>> graph(n, map<int, int>());
        for(auto edge: edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u].emplace(v, w);
            graph[v].emplace(u, w);
        }
        auto dijkstra = [&](int src, bool ban_neg) {
            vector<int> dists(n, 2e9);
            dists[src] = 0;
            vector<int> parent(n, -1);
            priority_queue<pair<int, int>,
                vector<pair<int, int>>,
                decltype([](auto p1, auto p2) {
                    return p1.first > p2.first;
                })> pq;
            pq.emplace(0, src);
            while(!pq.empty()) {
                auto [s, u] = pq.top();
                pq.pop();
                for(auto [v, w]: graph[u]) {
                    if(ban_neg && w == -1) continue;
                    if(w == -1) w = 1;
                    if(s + w < dists[v]) {
                        parent[v] = u;
                        dists[v] = s + w;
                        pq.emplace(s+w, v);
                    }
                }
            }
            return make_pair(dists, parent);
        };
        auto [d1, _] = dijkstra(source, true);
        if(d1[destination] < target) return {};
        auto [d2, parent] = dijkstra(source, false);
        if(d2[destination] > target) return {};
        
        // walk back from destination back to source using shortest path
        int u = destination;
        int walked = 0;
        while(u >= 0) {
            int p = parent[u];
            if(p >= 0) {
                if(graph[u][p] == -1) {
                    graph[u][p] = 1;
                    graph[p][u] = 1;
                    // if we found a way to p, p -> u (mutable node), u -> destination
                    // that can cost target, use that path, make all other mutable edge as 2e9
                    if(d1[p] + 1 + walked <= target) {
                        graph[u][p] = target - walked - d1[p];
                        graph[p][u] = target - walked - d1[p];
                        break;
                    }
                }
                walked += graph[u][p];
            }
            u = p;   
        }

        for(auto & edge: edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            edge[2] = graph[u][v] == -1 ? 2e9 : graph[u][v];
        }
        return edges;
    }
};
