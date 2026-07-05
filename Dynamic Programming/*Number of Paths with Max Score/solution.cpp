class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        int m = board.size(), n = board[0].size();
        int MOD = 1e9 + 7;
        vector<vector<pair<int, int>>> dp(m, vector<pair<int, int>>(n));
        dp[m-1][n-1] = {0, 1};
        vector<pair<int, int>> ds{{-1,0}, {0,-1}, {-1, -1}};
        for(int r = m-1; r >= 0; --r) {
            for(int c = n-1; c >= 0; --c) {
                if(board[r][c] == 'X') continue;
                for(auto [dr, dc]: ds) {
                    int pr = r - dr, pc = c - dc;
                    if(pr >= m || pc >= n || !dp[pr][pc].second) continue;
                    int v = board[r][c] == 'E' ? 0: (board[r][c] - '0');
                    if(dp[pr][pc].first + v > dp[r][c].first) {
                        dp[r][c] = {dp[pr][pc].first + v, dp[pr][pc].second};
                    } else if(dp[pr][pc].first + v == dp[r][c].first) {
                        dp[r][c].second = (dp[r][c].second + dp[pr][pc].second) % MOD;
                    }
                }
            }
        }

        return {dp[0][0].first, dp[0][0].second};

    }
};
