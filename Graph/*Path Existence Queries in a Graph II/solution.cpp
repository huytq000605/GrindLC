class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<pair<int, int>> inums;
        inums.reserve(n);
        for(int i = 0; i < n; ++i) {
            inums.emplace_back(i, nums[i]);
        }
        sort(begin(inums), end(inums), [](auto &p1, auto &p2) -> bool {
            return p1.second < p2.second;
        });
        int LOG = 1;
        while((1 << LOG) <= n) ++LOG;
        vector<vector<int>> L(LOG, vector<int>(n));
        vector<int> pos(n);
        for(int i = 0, j = 0; i < n; ++i) {
            while(inums[i].second - inums[j].second > maxDiff) ++j;
            L[0][i] = j;
            pos[inums[i].first] = i;
        }
        
        for(int k = 1; k < LOG; ++k) {
            for(int i = 0; i < n; ++i) {
                L[k][i] = L[k-1][L[k-1][i]];
            }
        }

        vector<int> result;
        result.reserve(queries.size());
        for(auto &q: queries) {
            int u = pos[q[0]], v = pos[q[1]];
            if(u == v) {
                result.push_back(0);
            } else {
                if(u < v) swap(u, v);
                int steps = 0;
                for(int i = LOG-1; i >= 0; --i) {
                    if(L[i][u] > v) {
                        u = L[i][u];
                        steps += (1 << i);
                    }
                }
                result.push_back(L[0][u] > v ? -1: steps + 1);
            }
        }
        return result;
    }
};
