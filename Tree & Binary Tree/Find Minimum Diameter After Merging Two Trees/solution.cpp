class Solution {
public:
    int minimumDiameterAfterMerge(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        auto build_tree = [](vector<vector<int>> &edges) {
            int n = edges.size() + 1;
            vector<vector<int>> tree(n);
            for(auto &e: edges) {
                int u{e[0]}, v{e[1]};
                tree[u].emplace_back(v);
                tree[v].emplace_back(u);
            }
            return tree;
        };
        auto tree1 = build_tree(edges1);
        auto tree2 = build_tree(edges2);
        auto find_diameter = [](vector<vector<int>> &tree) {
            deque<pair<int, int>> dq;
            dq.emplace_back(0, -1);
            int new_start{-1};
            while(!dq.empty()) {
                auto [u, p] = dq.front(); dq.pop_front();
                new_start = u;
                for(auto v: tree[u]) {
                    if(v == p) continue;
                    dq.emplace_back(v, u);
                }
            }

            int d{};
            dq.emplace_back(new_start, -1);
            while(!dq.empty()) {
                int k = dq.size();
                while(k--) {
                    auto [u, p] = dq.front(); dq.pop_front();
                    new_start = u;
                    for(auto v: tree[u]) {
                    if(v == p) continue;
                        dq.emplace_back(v, u);
                    }
                }
                ++d;
            }

            return d-1;
        };

        int d1 = find_diameter(tree1);
        int d2 = find_diameter(tree2);
        return max({d1, d2, (d1+1) / 2 + (d2 + 1) / 2 + 1});
    }
};
