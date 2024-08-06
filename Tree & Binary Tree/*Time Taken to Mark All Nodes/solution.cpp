class Solution {
public:
    vector<int> timeTaken(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> graph(n, vector<int>());
        for(auto e: edges) {
            int u = e[0], v = e[1];
            graph[u].emplace_back(v);
            graph[v].emplace_back(u);
        }
        auto cmp = [](auto p1, auto p2) {
                return p1.first > p2.first;
        };
        vector<vector<pair<int, int>>> times(n);
        for(int i = 0; i < n; i++) {
            times[i].emplace_back(0, -1);
        }

        auto add_time = [&](int u, int v, int t) {
            times[u].emplace_back(t, v);
            push_heap(times[u].begin(), times[u].end(), cmp);
            if(times[u].size() > 2) {
                pop_heap(times[u].begin(), times[u].end(), cmp);
                times[u].pop_back();
            }
        };

        auto dfs = [&](auto u, auto p, auto dfs_ref) -> int {
            for(auto v: graph[u]) {
                if(v == p) continue;
                auto t = dfs_ref(v, u, dfs_ref) + (v & 1 ? 1 : 2);
                add_time(u, v, t);
            }
            return times[u].size() == 2 ? times[u][1].first: times[u][0].first;
        };

        
        vector<int> result(n, 0);
        result[0] = dfs(0, -1, dfs);
        //   A -- D
        //  / | 
        // B   C
        // |
        // E
        // res(B) = max(times[B], B->A + max(times[child_A excl B]));
        // res(B) = max(times[B], parent_cost)
        // reroot from A to B
        // add parent_cost to child_B because now A is child of B.

        auto dfs2 = [&](auto u, auto p, auto dfs_ref) -> void {
            for(auto v: graph[u]) {
                if(v == p) continue;
                int parent_cost = (u & 1 ? 1 : 2) + (times[u].size() != 2 ? 0 : times[u][1].second == v ? times[u][0].first : times[u][1].first);
                result[v] = max(
                    times[v].size() == 2 ? times[v][1].first : times[v][0].first,
                    parent_cost
                );
                add_time(v, u, parent_cost);
                dfs_ref(v, u, dfs_ref);
            }
        };
        dfs2(0, -1, dfs2);
        return result;
    }
};
