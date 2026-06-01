class Solution {
public:
    vector<vector<int>> candyCrush(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        auto drop = [&]() -> void {
            for(int c = 0; c < n; ++c) {
                int rr = m-1;
                for(int r = m-1; r >= 0; --r) {
                    if(board[r][c]) {
                        board[rr][c] = board[r][c];
                        if(r != rr) board[r][c] = 0;
                        --rr;
                    }
                }
            }
        };

        auto crush = [&]() -> bool {
            vector<pair<int, int>> to_remove;
            for(int r = 0; r < m; ++r) {
                for(int c = 2; c < n;) {
                    int v = board[r][c];
                    if(v && board[r][c-1] == v && board[r][c-2] == v) {
                        for(c = c-2; c < n && board[r][c] == v; ++c) {
                            to_remove.emplace_back(r, c);
                        }
                    } else {
                        ++c;
                    }
                }
            }

            for(int c = 0; c < n; ++c) {
                for(int r=2; r < m;) {
                    int v = board[r][c];
                    if(v && board[r-1][c] == v && board[r-2][c] == v) {
                        for(r = r-2; r < m && board[r][c] == v; ++r) {
                            to_remove.emplace_back(r, c);
                        }
                    } else {
                        ++r;
                    }
                }
            }

            for(auto [r, c]: to_remove) board[r][c] = 0;
            return !to_remove.empty();
        };

        while(crush()) drop();
        return board;
    }
};
