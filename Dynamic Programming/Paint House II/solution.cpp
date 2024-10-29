class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        int n = costs.size(), k = costs[0].size();
        // dp[i][j1] = max(dp[i-1][j2 != j1]) + cost[i][j1]
        vector<pair<int, int>> top2{ {0, -1}, {0, -2} };
        auto cmp = [](auto &p1, auto &p2) -> bool {
            return p1.first < p2.first;
        };
        for(int house = 0; house < n; ++house) {
            vector<pair<int, int>> ntop2;
            for(int color = 0; color < k; ++color) {
                ntop2.emplace_back((color==top2.back().second ? top2.front().first : top2.back().first) + costs[house][color], color);
                push_heap(ntop2.begin(), ntop2.end(), cmp);
                if(ntop2.size() > 2) {
                    pop_heap(ntop2.begin(), ntop2.end(), cmp);
                    ntop2.pop_back();
                }
            }
            top2 = move(ntop2);
        }
        
        return top2[1].first;
    }
};
