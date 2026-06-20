class Solution {
public:
    int maxBuilding(int n, vector<vector<int>>& rs) {
        sort(begin(rs), end(rs), [](auto &r1, auto &r2) -> bool {
            return r1[0] < r2[0];
        });
        rs.insert(begin(rs), {1, 0});
        if(rs.back()[0] != n) {
            rs.push_back({n, INT_MAX});
        }
        int result = 0;
        for(int i = 1; i < rs.size(); ++i) {
            int d = rs[i][0] - rs[i-1][0];
            rs[i][1] = min(rs[i][1], rs[i-1][1] + d);
        }

        for(int i = rs.size() - 2; i >= 0; --i) {
            int d = rs[i+1][0] - rs[i][0];
            rs[i][1] = min(rs[i][1], rs[i+1][1] + d);
            int max_reach = max(rs[i][1], rs[i+1][1]);
            int dh = abs(rs[i+1][1] - rs[i][1]);
            if(d > dh) max_reach += (d - dh) / 2;
            result = max(result, max_reach);
        }
        return result;
    }
};
