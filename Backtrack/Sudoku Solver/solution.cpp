class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<vector<int>> rows(9, vector<int>(10)), cols(9, vector<int>(10)), squares(9, vector<int>(10));
        vector<pair<int, int>> to_solve;
        for(int r = 0; r < 9; ++r) {
            for(int c = 0; c < 9; ++c) {
                if(board[r][c] == '.') {
                    to_solve.emplace_back(r, c);
                    continue;
                }
                int v = board[r][c] - '0';
                rows[r][v] = 1;
                cols[c][v] = 1;
                int sq = r / 3 * 3 + c / 3;
                squares[sq][v] = 1;
            }
        }
        auto dfs = [&](this auto&& dfs, int i) {
            if(i >= to_solve.size()) return true;
            auto [r, c] = to_solve[i];
            int sq = r/3*3 + c/3;
            for(int v = 1; v <= 9; ++v) {
                if(rows[r][v] || cols[c][v] || squares[sq][v]) continue;
                rows[r][v] = 1;
                cols[c][v] = 1;
                squares[sq][v] = 1;
                board[r][c] = '0' + v;
                if(dfs(i+1)) return true;
                rows[r][v] = 0;
                cols[c][v] = 0;
                squares[sq][v] = 0;
                board[r][c] = '.';
            }
            return false;
        };
        cout << dfs(0) << endl;
    }
};
