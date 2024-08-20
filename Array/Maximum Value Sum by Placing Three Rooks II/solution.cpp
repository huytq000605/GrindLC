class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        auto cmp = [](auto a, auto b) {return a.second > b.second;};
        vector<vector<pair<int, long long>>> top3(m, vector<pair<int, long long>>());
        multiset<tuple<int, int, long long>, decltype([](auto p1, auto p2) {return get<2>(p1) > get<2>(p2);})> ms; 
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

        for(int r = 0; r < m; ++r) {
            for(auto [c, v]: top3[r]) {
                ms.emplace(r, c, v);
                if(ms.size() > 11) {
                    auto it = ms.rbegin();
                    ms.erase(*it);
                } 
            }
        }

        long long result = -3000000000;
        for(auto r1 = 0; r1 < m - 2; ++r1) {
            for(auto [c1, _]: top3[r1]) {
                for(int r2 = r1 + 1; r2 < m - 1; ++r2) {
                    for(auto [c2, _]: top3[r2]) {
                        if(c2 == c1) continue;
                        // for each (r1, c1), it makes at most 5 cells to be invalid
                        // => 2 rows cause at most 10 cells to be invalid
                        // => Take top 11
                        for(auto [r3, c3, v]: ms) {
                            if(r3 == r1 || r3 == r2 || c3 == c1 || c3 == c2) continue;
                            result = max(result, static_cast<long long>(board[r1][c1] + board[r2][c2]) + v);
                        }
                    }
                }
            }
        }
        return result;
    }
};
