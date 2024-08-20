class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        auto cmp = [](auto a, auto b) {return a.second > b.second;};
        vector<vector<pair<int, long long>>> top3(m, vector<pair<int, long long>>());
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                top3[r].emplace_back(c, board[r][c]);
                push_heap(top3[r].begin(), top3[r].end(), cmp);
                if(top3[r].size() > 3) {
                    pop_heap(top3[r].begin(), top3[r].end(), cmp);
                    top3[r].pop_back();
                }
            }
        }
        long long result = -3000000000;
        for(int r1 = 0; r1 < m - 2; ++r1) {
            for(auto [c1, _]: top3[r1]) {
                for(int r2 = r1 + 1; r2 < m - 1; ++r2) {
                    for(auto [c2, _]: top3[r2]) {
                        if(c2 == c1) continue;
                        for(int r3 = r2 + 1; r3 < m; ++r3) {
                            for(auto [c3, _]: top3[r3]) {
                                if(c3 == c2 || c3 == c1) continue;
                                long long s = static_cast<long long>(board[r1][c1] + board[r2][c2]) + board[r3][c3];
                                result = max(result, s);
                            }
                        }   
                    }
                }
            }
        }
        return result;
    }
};
