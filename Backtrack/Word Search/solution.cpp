class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        vector<pair<int, int>> ds{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int m = board.size(), n = board[0].size();
        std::function<bool(int, int, int)> dfs;
        dfs = [&](int r, int c, int i) -> bool {
            if(i >= word.size()) {
                return true;
            }
            for (auto d : ds) {
                auto dr = d.first, dc = d.second;
                auto nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n)
                    continue;
                if(board[nr][nc] != word[i]) continue;
                auto original = board[nr][nc];
                board[nr][nc] = '#';
                if (dfs(nr, nc, i + 1)) {
                    return true;
                }
                board[nr][nc] = original;
            }
            return false;
        };
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if(board[r][c] == word[0]) {
                    auto original = board[r][c];
                    board[r][c] = '#';
                    if(dfs(r, c, 1)) return true;
                    board[r][c] = original;
                }
            }
        }
        return false;
    }
};
