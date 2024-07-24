class Solution {
public:
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        auto fill = [&](auto & conditions) -> vector<int> {
            vector<unordered_set<int>> before(k, unordered_set<int>()), after(k, unordered_set<int>());
            for(auto cond: conditions) {
                auto u = cond[0] - 1;
                auto v = cond[1] - 1;
                after[u].emplace(v);
                before[v].emplace(u);
            }
            vector<int> can;
            vector<int> result(k);
            for(int i = 0; i < k; i++) {
                if(before[i].empty()) {
                    can.emplace_back(i);
                }
            }
            for(int i = 0; i < k; i++) {
                if(can.empty()) return {};
                int u = can.back();
                result[u] = i;
                can.pop_back();
                for(auto v: after[u]) {
                    before[v].erase(u);
                    if(before[v].empty()) can.emplace_back(v);
                }
            }
            return result;
        };
        
        auto rows = fill(rowConditions);
        if(rows.empty()) return {};
        auto cols = fill(colConditions);
        if(cols.empty()) return {};

        vector<vector<int>> result(k, vector<int>(k, 0));
        for(int i = 0; i < k; i++) {
            result[rows[i]][cols[i]] = i+1;
        }

        return result;
    }
};
