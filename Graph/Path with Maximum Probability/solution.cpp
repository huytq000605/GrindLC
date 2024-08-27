class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<vector<pair<int, double>>> graph(n, vector<pair<int, double>>());
        for(int i = 0; i < edges.size(); i++) {
            auto e = edges[i];
            graph[e[0]].emplace_back(e[1], succProb[i]);
            graph[e[1]].emplace_back(e[0], succProb[i]);
        }
        priority_queue<pair<double, int>, vector<pair<double, int>>,
            decltype([](auto p1, auto p2) -> bool { return p1.first < p2.first; })> pq;
        pq.emplace(1, start_node);
        vector<double> prob(n, 0);
        prob[start_node] = 1;
        while(!pq.empty()) {
            auto [pu, u] = pq.top();
            if(u == end_node) return pu;
            pq.pop();
            for(auto [v, pv]: graph[u]) {
                if(prob[v] < pu * pv) {
                    prob[v] = pu * pv;
                    pq.emplace(pu * pv, v);
                }
            }
        }
        return 0;
    }
};
