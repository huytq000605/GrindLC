int dp[50][50][50][50];
void pre() {
    static bool flag = false;
    if(flag) return;
    vector<pair<int, int>> ds = {{ {-1,-2}, {-1, 2}, {1, -2}, {1, 2}, {-2, 1}, {-2, -1}, {2, 1}, {2, -1} }};
    memset(dp, -1, sizeof(dp));
    for(int r1 = 0; r1 < 50; ++r1) {
        for(int c1 = 0; c1 < 50; ++c1) {   
            deque<tuple<int, int, int>> dq;
            dq.emplace_back(0, r1, c1);
            dp[r1][c1][r1][c1] = 0;
            while(!dq.empty()) {
                auto [s, r, c] = dq.front();
                if(r1 == 0 && c1 == 0) cout << r << " " << c << endl;
                dq.pop_front();
                for(auto &[dr, dc]: ds) {
                    int nr = r + dr, nc = c + dc;
                    if(nr < 0 || nr >= 50 || nc < 0 || nc >= 50 || dp[r1][c1][nr][nc] != -1) continue;
                    dp[r1][c1][nr][nc] = s+1;
                    dq.emplace_back(s+1, nr, nc);
                }
            }
        }
    }
    flag = 1;
}


class Solution {
public:
    int maxMoves(int kx, int ky, vector<vector<int>>& positions) {
        pre();
        int n = positions.size();
        positions.push_back({kx, ky});
        vector<vector<int>> memo(n+1, vector<int>(1 << n, -1));
        auto dfs = [&](int i, int mask, int player, auto dfs_ref) -> int {
            if(memo[i][mask] != -1) return memo[i][mask];
            if(mask == pow(2, n) - 1) return 0;
            int result;
            int r = positions[i][0], c = positions[i][1];
            if(player == 0) {
                result = 0;
                for(int i = 0; i < n; ++i) {
                    if((mask >> i) & 1) continue;
                    int nr = positions[i][0], nc = positions[i][1];
                    result = max(result, dp[r][c][nr][nc] + dfs_ref(i, mask | (1 << i), 1-player, dfs_ref));
                }
            } else {
                result = 50*50;
                for(int i = 0; i < n; ++i) {
                    if((mask >> i) & 1) continue;
                    int nr = positions[i][0], nc = positions[i][1];
                    result = min(result, dp[r][c][nr][nc] + dfs_ref(i, mask | (1 << i), 1-player, dfs_ref));
                }
            }
            return memo[i][mask] = result;
        };

        return dfs(n, 0, 0, dfs);
    }
};
