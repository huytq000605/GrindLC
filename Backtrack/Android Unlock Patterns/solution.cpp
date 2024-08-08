class Solution {
public:
    int numberOfPatterns(int m, int n) {
        auto skip = vector<vector<int>>(10, vector<int>(10, 0));
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5;
        
        auto at_most = [&](int k) {
            set<int> s;
            auto dfs = [&](auto k, auto u, auto dfs_ref) -> int{
                if(s.size() == k) return 1;
                int result = s.size() == 0 ? 0: 1;
                for(int v = 1; v <= 9; v++) {
                    if(s.find(v) != s.end()) continue;
                    if(skip[u][v] && s.find(skip[u][v]) == s.end()) continue;  
                    s.emplace(v);
                    result += dfs_ref(k, v, dfs_ref);
                    s.erase(v);
                }
                return result;
            };

            int result = dfs(k, 0, dfs);
            return result;
        };
        return at_most(n) - (m - 1 ? at_most(m-1): 0);
    }
};
