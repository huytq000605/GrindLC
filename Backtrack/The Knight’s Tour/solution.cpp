class Solution {
static constexpr array<pair<int, int>, 8> ds = {{ {-1, -2}, {-1, 2}, {-2, -1}, {-2, 1}, {1, -2}, {1, 2}, {2, -1}, {2, 1}}};
public:
    vector<vector<int>> tourOfKnight(int m, int n, int r, int c) {
        vector<vector<int>> board(m, vector<int>(n, -1));
        board[r][c] = 0;
        int i = 1;
        auto dfs = [&](int r, int c, auto dfs_ref) -> bool {
            if(i == m*n) return true;
            for(auto [dr, dc]: ds) {
                int nr = r+dr, nc = c+dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                if(board[nr][nc] != -1) continue;
                board[r+dr][c+dc] = i++;
                if(dfs_ref(r+dr, c+dc, dfs_ref)) return true;
                board[r+dr][c+dc] = -1;
                --i;
            }
            return false;
        };
        dfs(r, c, dfs);
        return board;
    }
};
