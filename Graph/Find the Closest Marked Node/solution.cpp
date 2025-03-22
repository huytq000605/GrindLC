class Solution {
public:
    int minimumDistance(int n, vector<vector<int>>& edges, int s, vector<int>& marked) {
        vector<vector<pair<int, int>>> graph(n);
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u].emplace_back(v, w);
        }
        vector<int> ds(n, INT_MAX);
        ds[s] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype([](auto &p1, auto &p2) {
            return p1.second > p2.second; 
        })> pq;
        pq.emplace(s, 0);
        unordered_set<int> marked_set(marked.begin(), marked.end()); 
        while(!pq.empty()) {
            auto [u, d] = pq.top(); pq.pop();
            if(marked_set.find(u) != marked_set.end()) {
                return d;
            }
            for(auto [v, w]: graph[u]) {
                if(d + w < ds[v]) {
                    pq.emplace(v, d + w);
                    ds[v] = d + w;
                }
            }
        }
        return -1;
    }
};
