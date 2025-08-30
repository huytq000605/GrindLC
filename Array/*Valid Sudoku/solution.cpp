class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> rows(9, vector<int>(10)), cols(9, vector<int>(10));
        vector<vector<int>> squares(9, vector<int>(10));
        for(int r = 0; r < 9; ++r) {
            for(int c = 0; c < 9; ++c) {
                if(board[r][c] == '.') continue;
                int v = board[r][c] - '0';
                if(rows[r][v]) return false;
                rows[r][v] = 1;
                if(cols[c][v]) return false;
                cols[c][v] = 1;
                int s = r / 3 * 3 + c / 3;
                if(squares[s][v]) return false;
                squares[s][v] = 1;
            }
        }
        return true;
    }
};
